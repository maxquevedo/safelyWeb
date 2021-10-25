--LISTA PLAN con servicios
create or replace procedure sp_listar_plan_planb(plan out SYS_REFCURSOR)
is
begin

    open plan for select * from plan 
    inner join servicio on plan.id_servicio = servicio.id_servicio;

    
end;

-- LISTAR SOLO SERVICIOS
create or replace procedure sp_listar_servicios(servicio out SYS_REFCURSOR)
is
begin

    open servicio for select * from servicio;
end;

--AGREGAR PLAN
create or replace procedure sp_agregar_plan(
    v_id_plan number,
    v_nombre varchar2,
    v_descripcion varchar2,
    v_id_servicio number,
    v_salida out number
)is
begin

    insert into plan(id_plan,nombre,descripcion,id_servicio)
    values(v_id_plan,v_nombre,v_descripcion,v_id_servicio);
    commit;
    v_salida:=1;

    exception
    
    when others then
        v_salida:=0;

end;

--Actualizar plan
create or replace procedure sp_actualizar_plan(
    v_id_plan number,
    v_nombre varchar2,
    v_descripcion varchar2,
    v_id_servicio number,
    v_salida out number
)is
begin

    UPDATE plan
    SET nombre = v_nombre, descripcion = v_descripcion, id_servicio = v_id_servicio
    WHERE id_plan = v_id_plan;
    commit;
        v_salida:=1;

    exception
    
    when others then
        v_salida:=0;

end;