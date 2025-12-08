/* ============================================================
   Proyecto: Ecotech Solutions Company
   Script:  schema.sql
   Función: Inicialización completa de la base de datos

   Este archivo crea:
   - La base de datos principal
   - El usuario administrador con permisos limitados al proyecto
   - Todas las tablas necesarias para el sistema de gestión
   - Llaves primarias, foráneas, índices y restricciones
   - Configuración estándar de timestamps y charset

   Requisitos del servidor:
   - MySQL 8.0 o superior
   - Motor de almacenamiento: InnoDB
   - Intercalación recomendada: utf8mb4_unicode_ci
   - Juego de caracteres: UTF8MB4 (soporta emojis y multilenguaje)

   Nota:
   Este script está diseñado para ejecutarse como usuario root
   mediante la herramienta init_db incluida en el proyecto.
   Modifica usuarios/contraseñas según sea necesario.
   ============================================================ */

DROP DATABASE IF EXISTS ecotech_solutions_company;

CREATE DATABASE ecotech_solutions_company;
USE ecotech_solutions_company;

CREATE USER IF NOT EXISTS 'ecotech_admin'@'localhost' IDENTIFIED BY 'Admin123!';
GRANT ALL PRIVILEGES ON ecotech_solutions_company.* TO 'ecotech_admin'@'localhost';
-- SELECT user, plugin FROM mysql.user;
-- En caso de que el plugin de autenticación sea sha256_password
-- ALTER USER 'ecotech_admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin123';
FLUSH PRIVILEGES;


-- -------------------------------------------------------
-- Tabla: usuarios
-- -------------------------------------------------------
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------------
-- Tabla: departamento
-- -------------------------------------------------------
CREATE TABLE departamento (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NULL,
    created_at TIMESTAMP NOT NULL
    	DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL
    	DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- índice para búsquedas por nombre
CREATE INDEX idx_departamento_nombre ON departamento (nombre);

-- -------------------------------------------------------
-- Tabla: proyecto
-- -------------------------------------------------------
CREATE TABLE proyecto (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT NULL,
    departamento_id INT NULL,
    fecha_inicio DATE NULL,
    fecha_fin DATE NULL,
    estado ENUM('planificado','activo','finalizado','cancelado') NOT NULL DEFAULT 'planificado',
    created_at TIMESTAMP NOT NULL
    	DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL
    	DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_proyecto_departamento FOREIGN KEY (departamento_id)
        REFERENCES departamento(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- índices útiles
CREATE INDEX idx_proyecto_nombre ON proyecto (nombre);
CREATE INDEX idx_proyecto_estado ON proyecto (estado);

-- -------------------------------------------------------
-- Tabla: empleado
-- -------------------------------------------------------
CREATE TABLE empleado (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(40) NULL,
    correo VARCHAR(200) NOT NULL UNIQUE,
    fecha_contrato DATE NULL,
    salario INT CHECK (salario >= 0),
    departamento_id INT NULL,
    proyecto_id INT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_empleado_departamento FOREIGN KEY (departamento_id)
        REFERENCES departamento(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT fk_empleado_proyecto FOREIGN KEY (proyecto_id)
        REFERENCES proyecto(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- índices para búsquedas por nombre / rut
CREATE INDEX idx_empleado_nombre ON empleado (nombre, apellido);
CREATE INDEX idx_empleado_codigo ON empleado (rut);


