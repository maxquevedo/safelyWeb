--auth_groups
insert into auth_group values(1,'Administrador');
insert into auth_group values(2,'Profesional');
insert into auth_group values(3,'Cliente');

--servicios
insert into servicio values(1,'prueba','pruebita',1);

--planes
insert into plan values(1,'Plan A','Dos visitas mensuales, doce asesorías mensuales, capacitaciones se cobran extra.',300000,1,1);

--tipo asesorias
insert into tipo_asesoria values(1,'Asesoria');
insert into tipo_asesoria values(2,'Accidente');
commit;