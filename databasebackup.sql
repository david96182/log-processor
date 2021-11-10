--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

-- Started on 2021-11-10 17:23:10 EST

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

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3014 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 203 (class 1259 OID 17244)
-- Name: req_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.req_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.req_id_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 200 (class 1259 OID 17141)
-- Name: requests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.requests (
    "time" timestamp without time zone NOT NULL,
    req character varying NOT NULL,
    status integer NOT NULL,
    bytes bigint NOT NULL,
    referer character varying,
    http_method character varying NOT NULL,
    sessionid character varying NOT NULL,
    requestid character varying NOT NULL
);


ALTER TABLE public.requests OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 17221)
-- Name: sessions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sessions (
    sessionid character varying NOT NULL,
    userid character varying NOT NULL,
    totalreq integer NOT NULL,
    totalpages integer NOT NULL,
    sessionlenght integer NOT NULL,
    totalbytes integer NOT NULL,
    timeperpage real NOT NULL,
    percof2xx real NOT NULL,
    percof3xx real NOT NULL,
    percof4xx real NOT NULL,
    percof5xx real NOT NULL,
    percofget real NOT NULL,
    percofpost real NOT NULL,
    percofput real NOT NULL,
    percofdelete real NOT NULL,
    percofpatch real NOT NULL,
    percofimgreq real NOT NULL,
    percofjscssreq real NOT NULL,
    percofofilereq real NOT NULL,
    standev2req real NOT NULL,
    prevhttpm integer NOT NULL,
    brospeed real NOT NULL,
    perofempref real NOT NULL
);


ALTER TABLE public.sessions OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 17148)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    userid character varying NOT NULL,
    ip character varying NOT NULL,
    useragent character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3005 (class 0 OID 17141)
-- Dependencies: 200
-- Data for Name: requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.requests ("time", req, status, bytes, referer, http_method, sessionid, requestid) FROM stdin;
\.


--
-- TOC entry 3007 (class 0 OID 17221)
-- Dependencies: 202
-- Data for Name: sessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sessions (sessionid, userid, totalreq, totalpages, sessionlenght, totalbytes, timeperpage, percof2xx, percof3xx, percof4xx, percof5xx, percofget, percofpost, percofput, percofdelete, percofpatch, percofimgreq, percofjscssreq, percofofilereq, standev2req, prevhttpm, brospeed, perofempref) FROM stdin;
\.


--
-- TOC entry 3006 (class 0 OID 17148)
-- Dependencies: 201
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (userid, ip, useragent) FROM stdin;
\.


--
-- TOC entry 3015 (class 0 OID 0)
-- Dependencies: 203
-- Name: req_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.req_id_seq', 1, false);


--
-- TOC entry 2868 (class 2606 OID 17243)
-- Name: requests requests_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.requests
    ADD CONSTRAINT requests_pk PRIMARY KEY (requestid);


--
-- TOC entry 2872 (class 2606 OID 17228)
-- Name: sessions sessions_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessions
    ADD CONSTRAINT sessions_pk PRIMARY KEY (sessionid);


--
-- TOC entry 2870 (class 2606 OID 17186)
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (userid);


--
-- TOC entry 2873 (class 2606 OID 17237)
-- Name: requests requests_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.requests
    ADD CONSTRAINT requests_fk FOREIGN KEY (sessionid) REFERENCES public.sessions(sessionid);


--
-- TOC entry 2874 (class 2606 OID 17229)
-- Name: sessions sessions_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessions
    ADD CONSTRAINT sessions_fk FOREIGN KEY (userid) REFERENCES public.users(userid);


-- Completed on 2021-11-10 17:23:10 EST

--
-- PostgreSQL database dump complete
--

