use summaraize;

CREATE TABLE interests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    useremailid VARCHAR(255),
    interests TEXT
);

CREATE TABLE newsfeedinfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain VARCHAR(255),
    json_path VARCHAR(255),
    videopath VARCHAR(255),
    time BIGINT,
    hash VARCHAR(255)
);
