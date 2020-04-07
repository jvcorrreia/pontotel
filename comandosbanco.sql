CREATE TABLE usuario(
   user_id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   senha VARCHAR (50) NOT NULL,
   email VARCHAR (355) UNIQUE NOT NULL
);

CREATE TABLE empresa(
   empresa_id serial PRIMARY KEY,
   nome VARCHAR (50) UNIQUE NOT NULL,
   cnpj VARCHAR (20) NOT NULL,
   sigla VARCHAR (5) UNIQUE NOT NULL
);

CREATE TABLE cotacao(
   cotacao_id serial PRIMARY KEY,
   empresa_id INT NOT NULL,
   cnpj VARCHAR (20) NOT NULL,
   data_cot date not null default CURRENT_DATE,
   alta float not null,
   baixa float not null,
	CONSTRAINT empresa_id FOREIGN KEY (empresa_id)
      REFERENCES empresa (empresa_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);