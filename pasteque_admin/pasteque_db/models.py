# coding: utf-8

# This models are managed by SQLAlchemy and NOT Django ORM
# This is because of the dynamic nature (e.g per user) of the pasteque databases

from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Index, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.mysql.base import BIT, MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Application(Base):
    __tablename__ = 'APPLICATIONS'

    id = Column('ID', String(255), primary_key=True)
    name = Column('NAME', String(255), nullable=False)
    version = Column('VERSION', String(255), nullable=False)

class CashRegister(Base):
    __tablename__ = 'CASHREGISTERS'

    id = Column('ID', Integer, primary_key=True)
    name = Column('NAME', String(255), nullable=False)
    location_id = Column('LOCATION_ID', ForeignKey(u'LOCATIONS.ID'),
        nullable=False, index=True)
    next_ticket_id = Column('NEXTTICKETID', Integer,
        nullable=False, server_default=text("'1'"))

    location = relationship(u'Location', backref='cash_registers')

class Location(Base):
    __tablename__ = 'LOCATIONS'

    id = Column('ID', String(255), primary_key=True)
    name = Column('NAME', String(255), nullable=False, unique=True)
    address = Column('ADDRESS', String(255))

class Module(Base):
    __tablename__ = 'MODULES'

    user_id = Column('user_id', Integer, primary_key=True)
    modules = Column('modules', Text, nullable=False)

class PaymentMode(Base):
    __tablename__ = 'PAYMENTMODES'

    id = Column('ID', Integer, primary_key=True)
    code = Column('CODE', String(255), nullable=False)
    name = Column('NAME', String(255), nullable=False)
    backname = Column('BACKNAME', String(255), nullable=False,
        server_default=text("''"))
    flags = Column('FLAGS', Integer, nullable=False,
        server_default=text("'0'"))
    active = Column('ACTIVE', BIT(1), nullable=False)
    system = Column('SYSTEM', BIT(1), nullable=False)
    disporder = Column('DISPORDER', Integer, nullable=False,
        server_default=text("'0'"))
    image = Column('IMAGE', MEDIUMBLOB)

class PaymentModeReturn(Base):
    __tablename__ = 'PAYMENTMODES_RETURNS'

    payment_mode_id = Column('PAYMENTMODE_ID', ForeignKey(u'PAYMENTMODES.ID'),
        primary_key=True, nullable=False)
    min_price = Column('MIN', Float(asdecimal=True), primary_key=True,
        nullable=False, server_default=text("'0'"))
    return_mode_id = Column('RETURNMODE_ID',
        ForeignKey(u'PAYMENTMODES.ID'), index=True)

    payment_mode = relationship(u'PAYMENTMODE',
        primaryjoin=lambda: PaymentModeReturn.payment_mode_id == PaymentMode.id)
    return_mode = relationship(u'PAYMENTMODE',
        primaryjoin=lambda: PaymentModeReturn.return_mode_id == PaymentMode.id)
