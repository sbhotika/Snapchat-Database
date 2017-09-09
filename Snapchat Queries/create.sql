-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2016-12-06 21:34:05.98

-- tables
-- Table: Advertisements
CREATE TABLE Advertisements (
    ad_id int  NOT NULL,
    order_id int  NOT NULL,
    cost real  NOT NULL,
    num_views int  NOT NULL,
    CONSTRAINT Advertisements_pk PRIMARY KEY (ad_id)
);

-- Table: Businesses
CREATE TABLE Businesses (
    business_id text  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Businesses_pk PRIMARY KEY (business_id)
);

-- Table: Orders
CREATE TABLE Orders (
    order_id int  NOT NULL,
    business_id text  NOT NULL,
    date_placed date  NOT NULL,
    CONSTRAINT Orders_pk PRIMARY KEY (order_id)
);

-- Table: Private_Snaps
CREATE TABLE Private_Snaps (
    to_username text  NOT NULL,
    snap_id int  NOT NULL,
    CONSTRAINT Private_Snaps_pk PRIMARY KEY (to_username,snap_id)
);

-- Table: Snappers
CREATE TABLE Snappers (
    username text  NOT NULL,
    name text  NOT NULL,
    location text  NOT NULL,
    snapscore int  NOT NULL,
    CONSTRAINT Snappers_pk PRIMARY KEY (username)
);

-- Table: Snaps
CREATE TABLE Snaps (
    snap_id int  NOT NULL,
    username text  NOT NULL,
    date_sent date  NOT NULL,
    seconds int  NOT NULL,
    CONSTRAINT Snaps_pk PRIMARY KEY (snap_id)
);

-- Table: Story
CREATE TABLE Story (
    story_id int  NOT NULL,
    snap_id int  NOT NULL,
    num_views int  NOT NULL,
    CONSTRAINT Story_pk PRIMARY KEY (story_id,snap_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Advertisements_1_Order (table: Advertisements)
ALTER TABLE Advertisements ADD CONSTRAINT Advertisements_1_Order
    FOREIGN KEY (order_id)
    REFERENCES Orders (order_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Businesses_Users (table: Businesses)
ALTER TABLE Businesses ADD CONSTRAINT Businesses_Users
    FOREIGN KEY (business_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Businesses (table: Orders)
ALTER TABLE Orders ADD CONSTRAINT Order_Businesses
    FOREIGN KEY (business_id)
    REFERENCES Businesses (business_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Private_Snaps_Snaps_1 (table: Private_Snaps)
ALTER TABLE Private_Snaps ADD CONSTRAINT Private_Snaps_Snaps_1
    FOREIGN KEY (snap_id)
    REFERENCES Snaps (snap_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Snappers_Users (table: Snappers)
ALTER TABLE Snappers ADD CONSTRAINT Snappers_Users
    FOREIGN KEY (username)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Snaps_1_Snappers (table: Snaps)
ALTER TABLE Snaps ADD CONSTRAINT Snaps_1_Snappers
    FOREIGN KEY (username)
    REFERENCES Snappers (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Story_Snaps (table: Story)
ALTER TABLE Story ADD CONSTRAINT Story_Snaps
    FOREIGN KEY (snap_id)
    REFERENCES Snaps (snap_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

