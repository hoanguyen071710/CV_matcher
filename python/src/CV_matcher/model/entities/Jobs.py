from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .Base import Base


class Jobs(Base):
    __tablename__ = "Jobs"
    __table_args__ = {"schema": "Jobs"}

    id: Mapped[int] = mapped_column(primary_key=True)
    site: Mapped[str] = mapped_column(String(255))
    job_url: Mapped[str] = mapped_column(String(255))
    job_url_direct: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255))
    company: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(255))
    job_type: Mapped[str] = mapped_column(String(255))
    date_posted: Mapped[str] = mapped_column(String(255))
    salary_source: Mapped[str] = mapped_column(String(255))
    interval: Mapped[str] = mapped_column(String(255))
    min_amount: Mapped[str] = mapped_column(String(255))
    max_amount: Mapped[str] = mapped_column(String(255))
    currency: Mapped[str] = mapped_column(String(255))
    is_remote: Mapped[str] = mapped_column(String(255))
    job_level: Mapped[str] = mapped_column(String(255))
    job_function: Mapped[str] = mapped_column(String(255))
    company_industry: Mapped[str] = mapped_column(String(255))
    listing_type: Mapped[str] = mapped_column(String(255))
    emails: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    company_url: Mapped[str] = mapped_column(String(255))
    company_url_direct: Mapped[str] = mapped_column(String(255))
    company_addresses: Mapped[str] = mapped_column(String(255))
    company_num_employees: Mapped[str] = mapped_column(String(255))
    company_revenue: Mapped[str] = mapped_column(String(255))
    company_description: Mapped[str] = mapped_column(String(255))
    logo_photo_url: Mapped[str] = mapped_column(String(255))
    banner_photo_url: Mapped[str] = mapped_column(String(255))
    ceo_name: Mapped[str] = mapped_column(String(255))
    ceo_photo_url: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f"""
            id: {self.id}
            site: {self.site}
            job_url: {self.job_url}
            job_url_direct: {self.job_url_direct}
            title: {self.title}
            company: {self.company}
            location: {self.location}
            job_type: {self.job_type}
            date_posted: {self.date_posted}
            salary_source: {self.salary_source}
            interval: {self.interval}
            min_amount: {self.min_amount}
            max_amount: {self.max_amount}
            currency: {self.currency}
            is_remote: {self.is_remote}
            job_level: {self.job_level}
            job_function: {self.job_function}
            company_industry: {self.company_industry}
            listing_type: {self.listing_type}
            emails: {self.emails}
            description: {self.description}
            company_url: {self.company_url}
            company_url_direct: {self.company_url_direct}
            company_addresses: {self.company_addresses}
            company_num_employees: {self.company_num_employees}
            company_revenue: {self.company_revenue}
            company_description: {self.company_description}
            logo_photo_url: {self.logo_photo_url}
            banner_photo_url: {self.banner_photo_url}
            ceo_name: {self.ceo_name}
            ceo_photo_url: {self.ceo_photo_url}
        """
    
    def all_key_values(self, exclude_primary_key=False):
        if exclude_primary_key:
            return {c.name: getattr(self, c.name) for c in self.__table__.columns if not c.primary_key}
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
