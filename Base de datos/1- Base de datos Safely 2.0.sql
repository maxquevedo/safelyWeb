CREATE TABLE actividad (
    id_actividad    INTEGER NOT NULL,
    nombre          VARCHAR2(250) NOT NULL,
    descripcion     VARCHAR2(250) NOT NULL,
    tipo_act        CHAR(1) NOT NULL,
    act_extra       NUMBER,
    fec_creacion    DATE,
    fec_estimada    DATE NOT NULL,
    fec_ida         DATE,
    estado          CHAR(1) NOT NULL,
    id_cli          INTEGER NOT NULL,
    id_prof         INTEGER,
    id_capacitacion INTEGER,
    id_asesoria     INTEGER,
    id_visita       INTEGER
);

ALTER TABLE actividad ADD CONSTRAINT actividad_pk PRIMARY KEY ( id_actividad );

CREATE TABLE administrador (
    id_admin  INTEGER NOT NULL,
    id_perfil INTEGER NOT NULL
);

ALTER TABLE administrador ADD CONSTRAINT administrador_pk PRIMARY KEY ( id_admin );

CREATE TABLE alerta (
    id_alerta   INTEGER NOT NULL,
    fec_aviso   DATE NOT NULL,
    descripcion VARCHAR2(300) NOT NULL,
    estado      NUMBER NOT NULL,
    id_cli      INTEGER NOT NULL,
    id_prof     INTEGER NOT NULL
);

ALTER TABLE alerta ADD CONSTRAINT alerta_pk PRIMARY KEY ( id_alerta );

CREATE TABLE asesoria (
    id_asesoria INTEGER NOT NULL,
    nombre      VARCHAR2(50) NOT NULL,
    descripcion VARCHAR2(250) NOT NULL,
    estado      NUMBER NOT NULL,
    id_tipo_ase INTEGER NOT NULL
);

ALTER TABLE asesoria ADD CONSTRAINT asesoria_pk PRIMARY KEY ( id_asesoria );

CREATE TABLE boleta (
    id_boleta       INTEGER NOT NULL,
    fec_emision_bol DATE NOT NULL,
    fec_pago        DATE NOT NULL,
    fec_corte       DATE NOT NULL,
    pago_mensual    INTEGER NOT NULL,
    pagado          NUMBER NOT NULL,
    pago_extra      INTEGER NOT NULL,
    url             VARCHAR2(250),
    id_contrato     INTEGER NOT NULL
);

ALTER TABLE boleta ADD CONSTRAINT boleta_pk PRIMARY KEY ( id_boleta );

CREATE TABLE capacitacion (
    id_capacitacion INTEGER NOT NULL,
    nombre          VARCHAR2(50) NOT NULL,
    cant_asistentes VARCHAR2(2) NOT NULL,
    materiales      VARCHAR2(250) NOT NULL,
    estado          NUMBER NOT NULL
);

ALTER TABLE capacitacion ADD CONSTRAINT capacitacion_pk PRIMARY KEY ( id_capacitacion );

CREATE TABLE checklist (
    id_check     INTEGER NOT NULL,
    nombre       VARCHAR2(1000) NOT NULL,
    verificacion NUMBER NOT NULL,
    fec_creado   DATE NOT NULL,
    id_clicheck  INTEGER NOT NULL
);

ALTER TABLE checklist ADD CONSTRAINT lista_pk PRIMARY KEY ( id_check );

CREATE TABLE cli_check_pro (
    id_clicheck INTEGER NOT NULL,
    id_prof     INTEGER,
    id_cli      INTEGER NOT NULL
);

ALTER TABLE cli_check_pro ADD CONSTRAINT cli_check_pk PRIMARY KEY ( id_clicheck );

CREATE TABLE cliente (
    id_cli       INTEGER NOT NULL,
    razon_social VARCHAR2(50) NOT NULL,
    id_perfil    INTEGER NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cli );

CREATE TABLE contrato (
    id_contrato INTEGER NOT NULL,
    fec_inicio  DATE NOT NULL,
    fec_termino DATE NOT NULL,
    total_pago  INTEGER NOT NULL,
    estado      NUMBER NOT NULL,
    id_plan     INTEGER NOT NULL,
    id_cli      INTEGER NOT NULL
);

ALTER TABLE contrato ADD CONSTRAINT contrato_pk PRIMARY KEY ( id_contrato );

CREATE TABLE mejora (
    id_mejora    INTEGER NOT NULL,
    nombre       VARCHAR2(50) NOT NULL,
    propuesta    VARCHAR2(250) NOT NULL,
    aceptacion   NUMBER NOT NULL,
    estado       NUMBER NOT NULL,
    id_actividad INTEGER NOT NULL
);

ALTER TABLE mejora ADD CONSTRAINT mejoras_pk PRIMARY KEY ( id_mejora );

CREATE TABLE perfil (
    id_perfil INTEGER NOT NULL,
    rut       VARCHAR2(12) NOT NULL,
    telefono  INTEGER NOT NULL,
    direccion VARCHAR2(200) NOT NULL,
    tipo_perf CHAR(1) NOT NULL,
    id_auth_user INTEGER NOT NULL
);

ALTER TABLE perfil ADD CONSTRAINT perfil_pk PRIMARY KEY ( id_perfil );

ALTER TABLE perfil ADD CONSTRAINT perfil__un UNIQUE ( rut );

CREATE TABLE plan (
    id_plan     INTEGER NOT NULL,
    nombre      VARCHAR2(20) NOT NULL,
    descripcion VARCHAR2(250) NOT NULL,
    costo       INTEGER NOT NULL,
    estado      NUMBER NOT NULL,
    id_servicio INTEGER NOT NULL
);

ALTER TABLE plan ADD CONSTRAINT plan_pk PRIMARY KEY ( id_plan );

CREATE TABLE profesional (
    id_prof   INTEGER NOT NULL,
    id_perfil INTEGER NOT NULL
);

ALTER TABLE profesional ADD CONSTRAINT profesional_pk PRIMARY KEY ( id_prof );

CREATE TABLE servicio (
    id_servicio INTEGER NOT NULL,
    nombre      VARCHAR2(20) NOT NULL,
    descripcion VARCHAR2(250) NOT NULL,
    estado      NUMBER NOT NULL
);

ALTER TABLE servicio ADD CONSTRAINT servicio_pk PRIMARY KEY ( id_servicio );

CREATE TABLE tipo_asesoria (
    id_tipo_ase INTEGER NOT NULL,
    nombre      VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_asesoria ADD CONSTRAINT tipo_asesoria_pk PRIMARY KEY ( id_tipo_ase );

CREATE TABLE visita (
    id_visita INTEGER NOT NULL,
    nombre    VARCHAR2(50) NOT NULL,
    estado    NUMBER NOT NULL
);

ALTER TABLE visita ADD CONSTRAINT visita_pk PRIMARY KEY ( id_visita );

ALTER TABLE cli_check_pro
    ADD CONSTRAINT act_check_cliente_fk FOREIGN KEY ( id_cli )
        REFERENCES cliente ( id_cli );

ALTER TABLE cli_check_pro
    ADD CONSTRAINT act_check_profesional_fk FOREIGN KEY ( id_prof )
        REFERENCES profesional ( id_prof );

ALTER TABLE actividad
    ADD CONSTRAINT actividad_asesoria_fk FOREIGN KEY ( id_asesoria )
        REFERENCES asesoria ( id_asesoria );

ALTER TABLE actividad
    ADD CONSTRAINT actividad_capacitacion_fk FOREIGN KEY ( id_capacitacion )
        REFERENCES capacitacion ( id_capacitacion );

ALTER TABLE actividad
    ADD CONSTRAINT actividad_cliente_fk FOREIGN KEY ( id_cli )
        REFERENCES cliente ( id_cli );

ALTER TABLE actividad
    ADD CONSTRAINT actividad_profesional_fk FOREIGN KEY ( id_prof )
        REFERENCES profesional ( id_prof );

ALTER TABLE actividad
    ADD CONSTRAINT actividad_visita_fk FOREIGN KEY ( id_visita )
        REFERENCES visita ( id_visita );

ALTER TABLE administrador
    ADD CONSTRAINT administrador_perfil_fk FOREIGN KEY ( id_perfil )
        REFERENCES perfil ( id_perfil );

ALTER TABLE alerta
    ADD CONSTRAINT alerta_cliente_fk FOREIGN KEY ( id_cli )
        REFERENCES cliente ( id_cli );

ALTER TABLE alerta
    ADD CONSTRAINT alerta_profesional_fk FOREIGN KEY ( id_prof )
        REFERENCES profesional ( id_prof );

ALTER TABLE asesoria
    ADD CONSTRAINT asesoria_tipo_asesoria_fk FOREIGN KEY ( id_tipo_ase )
        REFERENCES tipo_asesoria ( id_tipo_ase );

ALTER TABLE boleta
    ADD CONSTRAINT boleta_contrato_fk FOREIGN KEY ( id_contrato )
        REFERENCES contrato ( id_contrato );

ALTER TABLE checklist
    ADD CONSTRAINT checklist_act_check_fk FOREIGN KEY ( id_clicheck )
        REFERENCES cli_check_pro ( id_clicheck );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_perfil_fk FOREIGN KEY ( id_perfil )
        REFERENCES perfil ( id_perfil );

ALTER TABLE contrato
    ADD CONSTRAINT contrato_cliente_fk FOREIGN KEY ( id_cli )
        REFERENCES cliente ( id_cli );

ALTER TABLE contrato
    ADD CONSTRAINT contrato_plan_fk FOREIGN KEY ( id_plan )
        REFERENCES plan ( id_plan );

ALTER TABLE mejora
    ADD CONSTRAINT mejoras_actividad_fk FOREIGN KEY ( id_actividad )
        REFERENCES actividad ( id_actividad );

ALTER TABLE plan
    ADD CONSTRAINT plan_servicio_fk FOREIGN KEY ( id_servicio )
        REFERENCES servicio ( id_servicio );

ALTER TABLE profesional
    ADD CONSTRAINT profesional_perfil_fk FOREIGN KEY ( id_perfil )
        REFERENCES perfil ( id_perfil );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            17
-- CREATE INDEX                             0
-- ALTER TABLE                             37
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
