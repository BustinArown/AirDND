CREATE TABLE ListingDetails (
	bathrooms FLOAT(10,1),
	bedrooms INT,
	beds INT,
	location CHAR(50),
	id CHAR(40) NOT NULL,
	instantBookable BOOLEAN,
	isNewListing BOOLEAN,
	lat FLOAT,
	lng FLOAT,
	name CHAR(25),
	neighborhood CHAR(25),
	propertyType CHAR(15),
	reviewsCount INT,
	roomType CHAR(15),
	starRating FLOAT(1,1),
	userID INT NOT NULL,
	reviewID CHAR(40) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(userID) REFERENCES User(id),
	FOREIGN KEY(reviewID) REFERENCES Review(id)
);

CREATE TABLE User (
	acceptanceRate CHAR(10),
	createdAt DATETIME,
	friendsCount INT,
	hardSuspended BOOLEAN,
	id INT NOT NULL,
	listingsCount INT,
	publiclyVisibleWishlistsCount INT,
	recommendationCount INT,
	responseRate CHAR(10),
	responseTime CHAR(10),
	revieweeCount INT,
	softSuspended BOOLEAN,
	suspended BOOLEAN,
	totalListingsCount INT,
	wishlistsCount INT,
	PRIMARY KEY(id)
);

CREATE TABLE Review (
	comments CHAR(250),
	createdAt DATETIME,
	id CHAR(40) NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE Reservation (
	startDate DATETIME NOT NULL,
	endDate DATETIME NOT NULL,
	listingId CHAR(40) NOT NULL,
	PRIMARY KEY(startDate, endDate, listingID),
	FOREIGN KEY(listingId) REFERENCES ListingDetails(id)
);

CREATE TABLE Pricing (
	cost FLOAT NOT NULL,
	rateType CHAR(15) NOT NULL,
	listingID CHAR(40) NOT NULL,
	PRIMARY KEY(cost, rateType, listingID),
	FOREIGN KEY(listingID) REFERENCES ListingDetails(id)
);

CREATE TABLE Pagination (
	hasNextSection BOOLEAN,
	listingsOffset INT NOT NULL,
	sectionOffset INT NOT NULL,
	listingID CHAR(40) NOT NULL,
	PRIMARY KEY(listingOffset, sectionOffset, listingID),
	FOREIGN KEY(listingID) REFERENCES ListingDetails(id)
);