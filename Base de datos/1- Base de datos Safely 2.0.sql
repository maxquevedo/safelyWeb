-- Generado por Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   en:        2021-11-24 20:11:50 CLST
--   sitio:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

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
    url             VARCHAR2(250) NOT NULL,
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

CREATE TABLE chat (
    id_chat     INTEGER NOT NULL,
    mensaje     VARCHAR2(500) NOT NULL,
    fec_mensaje TIMESTAMP NOT NULL,
    enviado_por VARCHAR2(30) NOT NULL,
    cabecera    VARCHAR2(50) NOT NULL,
    id_prof     INTEGER NOT NULL,
    id_cli      INTEGER NOT NULL
);

ALTER TABLE chat ADD CONSTRAINT chat_pk PRIMARY KEY ( id_chat );

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

CREATE TABLE lista (
    id_lista      INTEGER NOT NULL,
    lista         VARCHAR2(1000) NOT NULL,
    verificacion  VARCHAR2(500) NOT NULL,
    recomendacion VARCHAR2(250) NOT NULL,
    id_actividad  INTEGER NOT NULL
);

ALTER TABLE lista ADD CONSTRAINT lista_pk PRIMARY KEY ( id_lista );

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
    id_perfil   INTEGER NOT NULL,
    rut         VARCHAR2(12),
    telefono    INTEGER,
    direccion   VARCHAR2(200),
    tipo_perf   CHAR(1),
    usuariop_id INTEGER NOT NULL
);

ALTER TABLE perfil ADD CONSTRAINT perfil_pk PRIMARY KEY ( id_perfil );

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

CREATE TABLE reporte (
    id_reporte      INTEGER NOT NULL,
    cant_asesoria   INTEGER NOT NULL,
    cant_llamadas   INTEGER NOT NULL,
    cant_visitas    INTEGER NOT NULL,
    cant_accidentes INTEGER NOT NULL,
    cant_multas     INTEGER NOT NULL,
    fec_emision     DATE NOT NULL,
    id_tipo_reporte INTEGER NOT NULL,
    id_actividad    INTEGER NOT NULL
);

ALTER TABLE reporte ADD CONSTRAINT reporte_pk PRIMARY KEY ( id_reporte );

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

CREATE TABLE tipo_reporte (
    id_tipo_reporte INTEGER NOT NULL,
    nombre          VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_reporte ADD CONSTRAINT tipo_reporte_pk PRIMARY KEY ( id_tipo_reporte );

CREATE TABLE usuariop (
    id INTEGER NOT NULL
);

ALTER TABLE usuariop ADD CONSTRAINT usuariop_pk PRIMARY KEY ( id );

CREATE TABLE visita (
    id_visita INTEGER NOT NULL,
    nombre    VARCHAR2(50) NOT NULL,
    estado    NUMBER NOT NULL
);

ALTER TABLE visita ADD CONSTRAINT visita_pk PRIMARY KEY ( id_visita );

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

ALTER TABLE chat
    ADD CONSTRAINT chat_cliente_fk FOREIGN KEY ( id_cli )
        REFERENCES cliente ( id_cli );

ALTER TABLE chat
    ADD CONSTRAINT chat_profesional_fk FOREIGN KEY ( id_prof )
        REFERENCES profesional ( id_prof );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_perfil_fk FOREIGN KEY ( id_perfil )
        REFERENCES perfil ( id_perfil );

ALTER TABLE contrato
    ADD CONSTRAINT contrato_cliente_fk FOREIGN KEY ( id_cli )
        REFERENCES cliente ( id_cli );

ALTER TABLE contrato
    ADD CONSTRAINT contrato_plan_fk FOREIGN KEY ( id_plan )
        REFERENCES plan ( id_plan );

ALTER TABLE lista
    ADD CONSTRAINT lista_actividad_fk FOREIGN KEY ( id_actividad )
        REFERENCES actividad ( id_actividad );

ALTER TABLE mejora
    ADD CONSTRAINT mejoras_actividad_fk FOREIGN KEY ( id_actividad )
        REFERENCES actividad ( id_actividad );

ALTER TABLE perfil
    ADD CONSTRAINT perfil_usuariop_fk FOREIGN KEY ( usuariop_id )
        REFERENCES usuariop ( id );

ALTER TABLE plan
    ADD CONSTRAINT plan_servicio_fk FOREIGN KEY ( id_servicio )
        REFERENCES servicio ( id_servicio );

ALTER TABLE profesional
    ADD CONSTRAINT profesional_perfil_fk FOREIGN KEY ( id_perfil )
        REFERENCES perfil ( id_perfil );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_actividad_fk FOREIGN KEY ( id_actividad )
        REFERENCES actividad ( id_actividad );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_tipo_reporte_fk FOREIGN KEY ( id_tipo_reporte )
        REFERENCES tipo_reporte ( id_tipo_reporte );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            20
-- CREATE INDEX                             0
-- ALTER TABLE                             42
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
