-- Criação da tabela Usuário 
CREATE TABLE Usuario ( 
    ID_Usuario SERIAL PRIMARY KEY, 
    Nome VARCHAR(100) NOT NULL, 
    Email VARCHAR(100) UNIQUE NOT NULL, 
    Senha VARCHAR(100) NOT NULL, 
    Perfil VARCHAR(50) NOT NULL 
); 
 
-- Criação da tabela Cliente 
CREATE TABLE Cliente ( 
    ID_Cliente SERIAL PRIMARY KEY, 
    Nome VARCHAR(100) NOT NULL, 
    Telefone VARCHAR(20), 
    Endereço TEXT, 
    Email VARCHAR(100) 
); 
 
-- Criação da tabela Produto 
CREATE TABLE Produto ( 
    ID_Produto SERIAL PRIMARY KEY, 
    Nome VARCHAR(100) NOT NULL, 
    Descricao TEXT, 
    Preco NUMERIC(10, 2) NOT NULL, 
    Categoria VARCHAR(50) 
); 
 
-- Criação da tabela Ordem de Serviço 
CREATE TABLE Ordem_Servico ( 
    ID_Ordem SERIAL PRIMARY KEY, 
    Data_Emissao DATE NOT NULL, 
    Status VARCHAR(50) NOT NULL, 
    ID_Usuario INT REFERENCES Usuario(ID_Usuario) ON DELETE CASCADE, 
    ID_Cliente INT REFERENCES Cliente(ID_Cliente) ON DELETE CASCADE 
); 
 
-- Criação da tabela Item_Ordem (tabela associativa entre Ordem_Servico e Produto) 
CREATE TABLE Item_Ordem ( 
    ID_Item_Ordem SERIAL PRIMARY KEY, 
    ID_Ordem INT REFERENCES Ordem_Servico(ID_Ordem) ON DELETE CASCADE, 
    ID_Produto INT REFERENCES Produto(ID_Produto) ON DELETE CASCADE, 
    Quantidade INT NOT NULL, 
    Preco_Unitario NUMERIC(10, 2) NOT NULL 
); 
 
-- Criação da tabela Estoque 
CREATE TABLE Estoque ( 
    ID_Estoque SERIAL PRIMARY KEY, 
    ID_Produto INT UNIQUE REFERENCES Produto(ID_Produto) ON DELETE CASCADE, 
    Quantidade_Disponivel INT NOT NULL, 
    Data_Atualizacao DATE NOT NULL 
); 
 
-- Adicionando comentários para melhorar a documentação das tabelas 
COMMENT ON TABLE Usuario IS 'Tabela que armazena os usuários do sistema.'; 
COMMENT ON TABLE Cliente IS 'Tabela que armazena os clientes associados às ordens de serviço.'; 
COMMENT ON TABLE Produto IS 'Tabela que armazena os produtos cadastrados no sistema.'; 
COMMENT ON TABLE Ordem_Servico IS 'Tabela que armazena as ordens de serviço criadas pelos usuários.'; 
COMMENT ON TABLE Item_Ordem IS 'Tabela associativa que relaciona produtos a ordens de serviço.'; 
COMMENT ON TABLE Estoque IS 'Tabela que armazena a quantidade disponível de cada produto no estoque.'; 