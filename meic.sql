--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Cadastro_Cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cadastro_Cliente" (
    "ID" integer NOT NULL,
    "Nome Completo" character varying(255) NOT NULL,
    "Data Nascimento" character(10) NOT NULL,
    "CPF" character(14) NOT NULL,
    "Telefone" character varying(14),
    "E-mail" character varying NOT NULL,
    "Senha" character varying(8) NOT NULL
);


ALTER TABLE public."Cadastro_Cliente" OWNER TO postgres;

--
-- Name: Cadastro_Ciente_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Cadastro_Cliente" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cadastro_Ciente_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Cadastro_Endereço; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cadastro_Endereço" (
    "ID" integer NOT NULL,
    "CEP" character varying(9) NOT NULL,
    "Nome_Rua" character varying(255) NOT NULL,
    "Numero" integer NOT NULL,
    "Complemento" character varying,
    "Nome_Bairro" character varying(255) NOT NULL,
    "Ponto_Referencia" character varying,
    "Cidade" character varying(255) NOT NULL,
    "Estado" character varying(255) NOT NULL,
    "ID_Cliente" integer NOT NULL
);


ALTER TABLE public."Cadastro_Endereço" OWNER TO postgres;

--
-- Name: Cadastro_Endereço_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Cadastro_Endereço" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cadastro_Endereço_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Cadastro_Loja; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cadastro_Loja" (
    "ID_Loja" integer NOT NULL,
    "Nome_Loja" character varying(255) NOT NULL,
    "CNPJ" character varying NOT NULL,
    "ID_Endereço" integer NOT NULL,
    "CPF_Usuario" character varying(14) NOT NULL
);


ALTER TABLE public."Cadastro_Loja" OWNER TO postgres;

--
-- Name: Cadastro_Loja_ID_Loja_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Cadastro_Loja" ALTER COLUMN "ID_Loja" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cadastro_Loja_ID_Loja_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Cadastro_Produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cadastro_Produto" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Categoria" character varying(255) NOT NULL,
    "Quantidade" integer NOT NULL,
    "Preço" character varying NOT NULL,
    "ID_Loja" integer NOT NULL
);


ALTER TABLE public."Cadastro_Produto" OWNER TO postgres;

--
-- Name: Cadastro_Produto_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Cadastro_Produto" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cadastro_Produto_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: Cadastro_Cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cadastro_Cliente" ("ID", "Nome Completo", "Data Nascimento", "CPF", "Telefone", "E-mail", "Senha") FROM stdin;
3	Douglas Viana	07/09/2001	123.456.789-10	85989589396	douglasviana49@gmail.com	12345
\.


--
-- Data for Name: Cadastro_Endereço; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cadastro_Endereço" ("ID", "CEP", "Nome_Rua", "Numero", "Complemento", "Nome_Bairro", "Ponto_Referencia", "Cidade", "Estado", "ID_Cliente") FROM stdin;
2	61600120	Rua Pedro Gomes da Rocha	31	abuble	Centro	abuble	Caucaia	CE	3
\.


--
-- Data for Name: Cadastro_Loja; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cadastro_Loja" ("ID_Loja", "Nome_Loja", "CNPJ", "ID_Endereço", "CPF_Usuario") FROM stdin;
2	Loja Teste	0616123045	2	123.456.789-10
\.


--
-- Data for Name: Cadastro_Produto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cadastro_Produto" ("ID", "Nome", "Categoria", "Quantidade", "Preço", "ID_Loja") FROM stdin;
10	Resma de A4	Papelaria	12	30,00 R$	2
\.


--
-- Name: Cadastro_Ciente_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cadastro_Ciente_ID_seq"', 3, true);


--
-- Name: Cadastro_Endereço_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cadastro_Endereço_ID_seq"', 2, true);


--
-- Name: Cadastro_Loja_ID_Loja_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cadastro_Loja_ID_Loja_seq"', 2, true);


--
-- Name: Cadastro_Produto_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cadastro_Produto_ID_seq"', 10, true);


--
-- Name: Cadastro_Cliente Cadastro_Ciente_CPF_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Cliente"
    ADD CONSTRAINT "Cadastro_Ciente_CPF_key" UNIQUE ("CPF");


--
-- Name: Cadastro_Cliente Cadastro_Ciente_E-mail_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Cliente"
    ADD CONSTRAINT "Cadastro_Ciente_E-mail_key" UNIQUE ("E-mail");


--
-- Name: Cadastro_Cliente Cadastro_Ciente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Cliente"
    ADD CONSTRAINT "Cadastro_Ciente_pkey" PRIMARY KEY ("ID");


--
-- Name: Cadastro_Endereço Cadastro_Endereço_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Endereço"
    ADD CONSTRAINT "Cadastro_Endereço_pkey" PRIMARY KEY ("ID");


--
-- Name: Cadastro_Loja Cadastro_Loja_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Loja"
    ADD CONSTRAINT "Cadastro_Loja_pkey" PRIMARY KEY ("ID_Loja");


--
-- Name: Cadastro_Produto Cadastro_Produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Produto"
    ADD CONSTRAINT "Cadastro_Produto_pkey" PRIMARY KEY ("ID");


--
-- Name: Cadastro_Loja fk_cadastro_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Loja"
    ADD CONSTRAINT fk_cadastro_cliente FOREIGN KEY ("CPF_Usuario") REFERENCES public."Cadastro_Cliente"("CPF") ON DELETE CASCADE;


--
-- Name: Cadastro_Endereço fk_cadastro_clientes; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Endereço"
    ADD CONSTRAINT fk_cadastro_clientes FOREIGN KEY ("ID_Cliente") REFERENCES public."Cadastro_Cliente"("ID") ON DELETE CASCADE;


--
-- Name: Cadastro_Loja fk_cadastro_endereço; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Loja"
    ADD CONSTRAINT "fk_cadastro_endereço" FOREIGN KEY ("ID_Endereço") REFERENCES public."Cadastro_Endereço"("ID") ON DELETE CASCADE;


--
-- Name: Cadastro_Produto fk_cadastro_loja; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cadastro_Produto"
    ADD CONSTRAINT fk_cadastro_loja FOREIGN KEY ("ID_Loja") REFERENCES public."Cadastro_Loja"("ID_Loja") ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

