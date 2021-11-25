create or replace procedure sp_listar_actividades(actividad out SYS_REFCURSOR)
is
begin
    open actividad for select * from productos;
end;

create or replace procedure sp_listar_capacitacion(capacitacion out SYS_REFCURSOR)
is
begin
open capacitacion for select * from capacitacion;
end;

create or replace procedure sp_listar_asesoria(asesoria out SYS_REFCURSOR)
is
begin
open asesoria for select * from asesoria;
end;

create or replace procedure sp_listar_visita(visita out SYS_REFCURSOR)
is
begin
open visita for select * from visita;
end;

create or replace procedure sp_listar_cliente(cliente out SYS_REFCURSOR)
is
begin
    open cliente for select * from cliente;
end;

create or replace procedure sp_listar_profesional(profesional out SYS_REFCURSOR)
is
begin
    open profesional for select * from profesional;
end;

create or replace procedure sp_agregar_actividad_corta(
    V_NOMBRE    VARCHAR2,
    V_DESCRIPCION	VARCHAR2,
    V_TIPO_ACT	CHAR,
    V_FEC_ESTIMADA	DATE,
    V_ESTADO    CHAR,
    V_ID_CLI	NUMBER,
    V_ID_PROF	NUMBER,
    V_SALIDA OUT NUMBER
) is
begin
     insert into actividad(nombre,descripcion,tipo_act,fec_estimada,estado,id_cli,id_prof)
     values(V_NOMBRE,V_DESCRIPCION,V_TIPO_ACT,V_FEC_ESTIMADA,V_ESTADO,V_ID_CLI,V_ID_PROF);
     commit;
     
     V_SALIDA:=1;
     exception 
     when others then
     V_SALIDA:=0;
end;

--Lista TODOS los datos del usuario- perfil
create or replace procedure sp_listar_usuario_perfil(perfil out SYS_REFCURSOR)
is
begin
    open perfil for select a.id,a.last_login,a.username,a.first_name,a.last_name,a.email,a.is_active,a.date_joined,
                            b.id_perfil,b.rut,b.telefono,b.direccion,b.tipo_perf from auth_user a full outer join perfil b
                            on a.id = b.id_auth_user order by a.id;
end;

--Lista datos cliente-perfil-usuario
create or replace procedure sp_listar_datos_cliente(cliente out SYS_REFCURSOR)
is
begin
    open cliente for --Trea solo datos importantes de cliente
select c.id ,c.username,c.first_name,c.last_name,c.email,
b.id_perfil,b.rut, b.telefono,b.direccion,
a.id_cli,a.razon_social
from cliente a join perfil b 
on a.id_perfil = b.id_perfil 
join auth_user c 
on b.id_auth_user = c.id;
end;