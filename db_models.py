class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)

    name = Column(String(100))
    website = Column(String(255), nullable=True)
    address = Column(String(100))
    phone = Column(String(100), nullable=True)
    rating = Column(Float, nullable=True)
    hours = Column(TEXT, nullable=True)
    description = Column(TEXT, nullable=True)
    detailed_description = Column(TEXT, nullable=True)
    category = Column(TEXT, nullable=True)
    service_options = Column(TEXT, nullable=True)
    filter = Column(TEXT, nullable=True)
    amenities = Column(TEXT, nullable=True)
    specialties = Column(TEXT, nullable=True)
    history = Column(TEXT, nullable=True)
    payment_options = Column(TEXT, nullable=True)
    company_url = Column(TEXT, nullable=True)

    created_at = Column(DateTime, default=func.now())

    source_id = Column(Integer, ForeignKey('source.id', ondelete="CASCADE"), nullable=False)

    reviews = relationship('Review', back_populates='company')
    photos = relationship('Photo', back_populates='company')
    source = relationship('Source', back_populates='companies')


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)

    author_name = Column(String(100))
    text = Column(TEXT, nullable=True)
    author_url = Column(TEXT, nullable=True)
    posted_at = Column(DateTime, nullable=True)
    author_photo_url = Column(TEXT, nullable=True)
    rating = Column(Float, nullable=True)

    created_at = Column(DateTime, default=func.now())

    company_id = Column(Integer, ForeignKey('company.id', ondelete="CASCADE"), nullable=False)

    company = relationship('Company', back_populates='reviews')
    photos = relationship('Photo', back_populates='review')


class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    photo_link = Column(TEXT, nullable=True)
    video_link = Column(TEXT, nullable=True)
    created_at = Column(DateTime, default=func.now())

    company_id = Column(Integer, ForeignKey('company.id', ondelete="CASCADE"), nullable=False)
    review_id = Column(Integer, ForeignKey('review.id', ondelete="CASCADE"), nullable=True)

    company = relationship('Company', back_populates='photos')
    review = relationship('Review', back_populates='photos')


class Source(Base):
    __tablename__ = 'source'

    id = Column(Integer, primary_key=True)

    name = Column(String(255))

    companies = relationship('Company', back_populates='source')