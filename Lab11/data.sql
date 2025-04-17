-- Создание таблицы
DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- 1. Функция поиска по шаблону
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE username ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Процедура вставки или обновления одного пользователя
CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = name) THEN
        UPDATE phonebook SET phone = phone WHERE username = name;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES (name, phone);
    END IF;
END;
$$;

-- 3. Процедура массовой вставки с проверкой
CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[], OUT invalid_data TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT := 1;
BEGIN
    invalid_data := ARRAY[]::TEXT[];
    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] ~ '^\+?[0-9]{7,15}$' THEN
            CALL insert_or_update_user(names[i], phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;

-- 4. Функция пагинации
CREATE OR REPLACE FUNCTION get_paginated_users(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook ORDER BY id LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;

-- 5. Процедура удаления по имени или телефону
CREATE OR REPLACE PROCEDURE delete_user(input TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook WHERE username = input OR phone = input;
END;
$$;
