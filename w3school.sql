create table cars(
brand varchar(255),
model varchar(255),
year int
);



select * from cars;

insert into cars(brand,model,year) values('Ford','Mustang',2964);

update cars set year=1964 where model='Mustang'; 

INSERT INTO CARS (brand,model,year)
VALUES	
('Volvo','P1800',1968),
('BMW','M1',1978),
('Toyota','Celica',1975);


select brand,year from cars; 

alter table cars 
add color varchar(255);

select * from cars;

update cars 
set color='red'
where brand='Volvo';

select * from cars;


update cars 
set color='red';

select * from cars;


update cars
set color='white', year=1970
where brand='Toyota';

select * from cars;


alter table cars
alter column year type varchar(4);

alter table cars
alter column color type varchar(30);


alter table cars
drop column color;

select * from cars;

delete from cars
where brand='Volvo';

select * from cars;

delete from cars;

truncate table cars;

drop table cars;
