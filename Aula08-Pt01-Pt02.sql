##### WORKBENCH #####

# PARTE 01

# Criar banco de dados
CREATE DATABASE empresaX;

# Usar banco de dados
USE empresaX;

# Criar tabela usuário
CREATE TABLE if not exists usuario(
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);
CREATE TABLE if not exists telefone(
  id_telefone INT NOT NULL AUTO_INCREMENT,
  numero INT NOT NULL,
  tipo VARCHAR(45) NOT NULL,
  id_usuario INT,
  PRIMARY KEY (id_telefone),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
# Carregar Schemas mostrar as tabela criadas

# Altera tabela usuario adicionar coluna cidade
ALTER TABLE usuario ADD COLUMN cidade VARCHAR(30);
# Carregar Schemas mostrar a coluna cidade adicionada

# Alterar tabela usuario deletar coluna cidade
ALTER TABLE usuario DROP COLUMN cidade;
# Carregar Schemas mostrar a coluna cidade deletada

# Apagar tabelas do banco de dados
# DROP TABLE telefone;
# DROP TABLE usuario;
# Falar da ordem de apagar: Não podemos apagar usuario antes de telefone. 
# Pois telefone tem uma chave estrangeira que referencia usuario.


# Apagar banco de dados
# DROP DATABASE empresaX;











# PARTE 02

# Inserir registros em usuario (não preciso informar id porque é auto incrementável)
INSERT INTO usuario(nome, senha, email) VALUES('Ana','ana2016','ana@gmail.com');
INSERT INTO usuario(nome, senha, email) VALUES('Giuliano','giu2016','giu@gmail.com');
INSERT INTO usuario(nome, senha, email) VALUES('Daniel','dani2016','dani@gmail.com');
# Select: Selecionar ou seja retornar todos os registro inseridos
select * from usuario;
# Verificar os ids que foram gerados automaticamente e incrementáveis


# Inserir registros em telefone (não preciso informar id_telefone porque é auto incrementável)
# Utilizar ids da tabela cliente
INSERT INTO telefone(numero, tipo, id_usuario) VALUES(987553663,'celular',1);
INSERT INTO telefone(numero, tipo, id_usuario) VALUES(34545937,'casa',1);
INSERT INTO telefone(numero, tipo, id_usuario) VALUES(977665544,'celular',2);
INSERT INTO telefone(numero, tipo, id_usuario) VALUES(911223344,'celular',3);
# Select: Selecionar ou seja retornar todos os registro inseridos
select * from telefone;

# Alterar dados em telefone
UPDATE telefone SET numero=988556644 WHERE id_telefone=1;
# Select: Selecionar ou seja retornar o registro alterado
select * from telefone;  

# Deletar dados em usario
# (Antes de deletar precisamos verificar se o registro não é referenciado por outra tabela)
DELETE FROM usuario WHERE id=3; 
# ERRO NA TELA (usuário id=13(Daniel) é referenciado por telefone- Daniel possui 1 telefone)
select * from usuario;
select * from telefone;

# Eu precisaria apagar o telefone primeiro e depois o usuário Daniel
DELETE FROM telefone WHERE id_usuario=3;
DELETE FROM usuario WHERE id=3;


# SELECT: Comando mais utilizado (Realiza consultas/pesquisas em históricos, informações salvas)
# Nos já vimos como selecionar todos os registro de uma tabela
SELECT * FROM usuario;

# Agora vamos utilizar o WHERE (onde): determina exatamente quais linhas devem ser recuperadas.
SELECT email FROM usuario WHERE id=1 and nome LIKE 'Ana';

# Comando in (em) : Retornar os dois primeiro usarios do sistema
SELECT * FROM telefone WHERE tipo IN ('casa','celular');

# Comando between (entre): Retornar 50 primeiros usuários
SELECT * FROM usuario WHERE id BETWEEN 1 and 50;

# Funções: realizar operações no select (soma, media,maximo, minimo, contador)
SELECT COUNT(id) FROM usuario;

# Comando Group by: Divide os dados em grupos
SELECT id_usuario,COUNT(numero) FROM telefone GROUP BY id_usuario;

# Comando order by: Ordena a consulta de acordo com uma coluna
SELECT * FROM usuario ORDER BY nome;

# Select com união (relacionamento) entre tabelas. São duas formas:
# 1. Usando as chaves primarias e estrangeiras
SELECT nome,numero FROM usuario,telefone WHERE usuario.id=telefone.id_usuario;

# 2. Usando inner join
SELECT nome,numero FROM usuario INNER JOIN telefone ON usuario.id=telefone.id_usuario;