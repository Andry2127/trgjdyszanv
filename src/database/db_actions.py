from typing import List
from uuid import uuid4

from src.database.models import Product, Review, User
from src.database.base import db

def get_products() -> List[Product]:
    return db.session.query(Product).all()


def get_product(prod_id: str) -> Product:
    return db.one_or_404(db.session.query(Product).where(Product.id == prod_id))

def add_product(name: str, description: str, img_url: str, price: float) ->str:
    product = Product(
        id=uuid4().hex,
        name=name,
        description=description,
        img_url=img_url,
        price=price

    )
    db.session.add(product)
    db.session.commit()
    return product.id


def update_product(prod_id: str, name: str, description: str, img_url: str, price: float):
    product = db.one_or_404(db.session.query(Product).where(Product.id == prod_id))
    product.name = name
    product.description = description
    product.img_url = img_url
    product.price = price
    db.session.commit()


def del_product(prod_id: str):
    product = db.one_or_404(db.session.query(Product).where(Product.id == prod_id))
    db.session.delete(product)
    db.session.commit()


def add_review_by_product(prod_id: str ,review: str,text: str, grade: str):
    review = Review(
        id=uuid4().hex,
        text=text,
        grade=grade

    )


    product = db.one_or_404(db.session.query(Product).where(Product.id == prod_id))
    product.reviews.append(review)
    db.session.commit()



def add_user(email: str, password: str, first_name: str|None = None, last_name: str|None = None):
    user = User(
        id=uuid4().hex,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return "Success"


def get_tokens(email: str,password: str) -> dict:
    user = db.one_or_404(db.session.query(User).where(User.email==email))
    return user.create_tokens(password)


def get_user(user_id: str):
    return db.one_or_404(db.session.query(User).where(User.id==user_id))


def get_review() -> List[Review]:
    return db.session.query(Review).all()


def get_reviews(review_id: str) -> Review:
    return db.one_or_404(db.session.query(Review).where(Review.id == review_id))

def add_review(text: str, grade: int) ->str:
    review = Review(
        id=uuid4().hex,
        review=review,
        grade=grade
    )
    db.session.add(review)
    db.session.commit()
    return review.id


def update_review(review_id: str, text: str, grade: int):
    review = db.one_or_404(db.session.query(Review).where(Review.id == review_id))
    review.text=text
    review.grade=grade
    db.session.commit()


def del_review(review_id: str):
    review = db.one_or_404(db.session.query(Review).where(Review.id == review_id))
    db.session.delete(review)
    db.session.commit()




