--Secuencias Safely--

--Actividad--

CREATE SEQUENCE actividad_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE actividad MODIFY (id_actividad DEFAULT actividad_seq.NEXTVAL);

--Alerta--

CREATE SEQUENCE alerta_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE alerta MODIFY (id_alerta DEFAULT alerta_seq.NEXTVAL);

--Asesoria--

CREATE SEQUENCE asesoria_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE asesoria MODIFY (id_asesoria DEFAULT asesoria_seq.NEXTVAL);

--Capacitaci�n--

CREATE SEQUENCE capacitacion_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE capacitacion MODIFY (id_capacitacion DEFAULT capacitacion_seq.NEXTVAL);

--Contrato--

CREATE SEQUENCE contrato_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE contrato MODIFY (id_contrato DEFAULT contrato_seq.NEXTVAL);


--Mejoras --

CREATE SEQUENCE mejora_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE mejora MODIFY (id_mejora DEFAULT mejora_seq.NEXTVAL);

--Plan--

CREATE SEQUENCE plan_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE plan MODIFY (id_plan DEFAULT plan_seq.NEXTVAL);

--Servicio--

CREATE SEQUENCE servicio_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE servicio MODIFY (id_servicio DEFAULT servicio_seq.NEXTVAL);

--tipo_asesoria--

CREATE SEQUENCE tipo_ase_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;

ALTER TABLE tipo_asesoria MODIFY (id_tipo_ase DEFAULT tipo_ase_seq.NEXTVAL);

--Visita--

CREATE SEQUENCE visita_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE visita MODIFY (id_visita DEFAULT visita_seq.NEXTVAL);

--Boleta--

CREATE SEQUENCE boleta_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
ALTER TABLE boleta MODIFY (id_boleta DEFAULT boleta_seq.NEXTVAL);

--Administrador--

CREATE SEQUENCE administrador_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE administrador MODIFY (id_admin DEFAULT administrador_seq.NEXTVAL);

--Cliente--

CREATE SEQUENCE cli_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE cliente MODIFY (id_cli DEFAULT cli_seq.NEXTVAL);

--Perfil --

CREATE SEQUENCE perfil_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE perfil MODIFY (id_perfil DEFAULT perfil_seq.NEXTVAL);

--Profesional--

CREATE SEQUENCE prof_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE profesional MODIFY (id_prof DEFAULT prof_seq.NEXTVAL);

--ACT-CHECK--

CREATE SEQUENCE cli_check_pro_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE cli_check_pro MODIFY (id_clicheck DEFAULT cli_check_pro_seq.NEXTVAL);

--CHECKLIST--

CREATE SEQUENCE checklist_seq
    START WITH     1
    INCREMENT BY   1
    NOCACHE
    NOCYCLE;
    
ALTER TABLE checklist MODIFY (id_check DEFAULT checklist_seq.NEXTVAL);

ALTER TABLE PERFIL
ADD CONSTRAINT PERFIL_AUTH_USER_FK FOREIGN KEY
(
  ID_AUTH_USER 
)
REFERENCES AUTH_USER
(
  ID 
)
ENABLE;