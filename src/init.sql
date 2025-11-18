
-- input
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    article_name TEXT NOT NULL,
    article_url TEXT NOT NULL UNIQUE
);

INSERT INTO articles (article_name, article_url) VALUES
(
    'Laozi',
    'https://test-ai-parser.obs.cn-north-4.myhuaweicloud.com:443/laozi.pdf?AccessKeyId=HSTAPYGUNHZGYORQ5JYE&Expires=1763514466&x-obs-security-token=hQpjbi1zb3V0aC0xAQAABDRIU1RBUFlHVU5IWkdZT1JRNUpZRUAvTMOxxRMe_qKELDqDgEbAA5kGHWNYE-LnnVa3AdHAVdv3emYVC0iwyubYKNeZvqj3HRicGXhJ6YuOxBoqtW-vXU9w5Yk17I_quXqN87bulGNy05Bo3O_EJL-WpsNfopo1JusY01h5nXaUJ3p3Rszu-OWF2TjEUUcEpDfAeQlol53HbbgM5W-nM0jKXS9_JpS92-b5O8rZ7lqjIQO6n9TqickkY3AP7_Vpp1zvzVfd_03bBqCAjyrgvDRT2O7yLQGtNRhvQp4RE0-RGGaSfBpLkuk8pNcaL-dZTSJEBKEgVAEC_rrEmp_ClhLXI9Q2u1xaY8xyQEbU6R1utp_c5L1n5clohJd9ZCR4VmAcbUow96MfT6J4D4Hud8xCWX4XH0Irk8QnMZDGuN5hLpTKoGiHD5roKoAFJIHcpIc7ul9hiNeAla5dfIA5Fv2RWA0CrANQNEpr6rY4r0aouzCTOejFpsE3k6dT0pI6JjdlE86x_Jum8nVYV2kM7SkcATaRHXB4i-io8_ed8Sji0t9B47lFHB5eJTVLvb-IkrpdbT_ZtYHM7ACbNso1H-9r_vWHGV1R_95lRwdRE5DvKyZmb-bdag%3D%3D&Signature=Td3QnIi8rv72lcFl9tgPI%2Bp2sJ0%3D'
),
(
    'Mao Zedong',
    'https://test-ai-parser.obs.cn-north-4.myhuaweicloud.com:443/mao.pdf?AccessKeyId=HSTA7I42DKS5M5E0O465&Expires=1763514498&x-obs-security-token=hQpjbi1zb3V0aC0xAQAABDRIU1RBN0k0MkRLUzVNNUUwTzQ2NRI4S7Lqtv8DZCSSJFJk_BiIAggdhnw8HTAJRQn_DcJDAWIGZsMZItiHwray5iNyk5VOeWtGhmw_evYwjX27TZBPViqwrtA6C0d3Ji6q0VXS5NTjLgxZ9E_BkRcEXUruo2D-at8FOHg7732phNBykycAx17J5ZiUnVAWZTaRkWigC7xsWuW2yyD0Zqd2ZGn8ByU18PjB-FSWn174GdwetxV7Q0dBc4ExGB7566VQSycW5rmsQnVTPZwIsZtBYVxxc_rI7y3qpYoLSEVS5TRah_3U2LwbPeYyHCo2RYlLvL1JK1--fYcbNG3o9AObD8o9VprmfjHlk97hr-Hejx72UWYbIUVByKQy3PeqGZdphH2EbGMi5xmZ-tYM1eq5Bd5dV9gRCFsQFlCRiMM-xQ7WLtWreZLCrsTm_IK9bLLLmH1JS0kxSlYHznhFqhTwg6PImMmJkMOccEAOma8m8RN7EZb7M6uc7oJPx8G9eg4--Mot-fWL6ERQTrEAk8-ymq-qz4qMIxEwRcezm24w_J62V1d1dHUVXP-WJlWakXkINPoJzfbYhlVt8CQFY3RS4B4o7CX_9PyC6c6UlbRSmxUDVw%3D%3D&Signature=wgx25D%2B/n%2B0pv1wJ0G43Uv/fa40%3D'
),
(
    'Shakespeare',
    'https://test-ai-parser.obs.cn-north-4.myhuaweicloud.com:443/shakespeare.pdf?AccessKeyId=HSTAMDX4VSDQ8L5P924N&Expires=1763514516&x-obs-security-token=hQpjbi1zb3V0aC0xAQAABDRIU1RBTURYNFZTRFE4TDVQOTI0TsO3bV8Wsihnf4SPqua7iJTecy1CxOj4-y1I6-FivGJ9kcQ8KjrwhprIEiz-5RZ_-IiyExmGtpJKQA2-Pah9n3ltkh0G8ymbyOaU4eciU9Fhqbrl-OPwwhaGXBGIN9Lo-XJRLKABq-AiJEV8xIvAHHX0myjgXBRaVQhvTFhqFd0RIVTZU6oVT_CAaPpysDULpPrggbYXTIu1wiSTDRCNo1HtqS_rP5C2f25GcWnLNsqQCmet1xrOTvoVIWrYe2oJKeFvJx5VsbHJ17pdS0bkuog7uSNzts1_hlaNUafre__rmq4ADPXRJmUnkC4xH-HA7iqnlpEj1E9wW-t854zmHwehgKeeN4iTGGlxP3NB33LMP232X4jmVqNGjoxaZw_xYQPEavXa3OT9SxWgt_JKlqm0CgbJUdOk8cEc4GdU3C4fW0lNBe_TsXMlDQFP4x1ckTKyrcZp4kzb2tYGDiGtm3nYv8SYZnFwKSeuGDIc4jh1uq0UeZw604-mNbEmFvMU4zUuKZbt2PClt8muMkl6F8C1XyUrlnm3YLMTSBUU5cHQUTLtUoaAlxA28xQVP68fmWJpzkwmWe6ydJsWINQV3p6yx-Y%3D&Signature=5d0qGsOwXEWf%2B2nGBVqsSL9u27Q%3D'
);

SELECT * FROM articles;


-- output

CREATE TABLE article_content (
    id SERIAL PRIMARY KEY,
    article_id INT NOT NULL,
    content JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT fk_article
        FOREIGN KEY(article_id)
        REFERENCES articles(id)
        ON DELETE CASCADE
);