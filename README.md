# Django Online Shop

A comprehensive online shop application with a Django backend and a JavaScript/HTML/CSS frontend. This project is built for scalability and rich e-commerce features, including user accounts, shopping cart, product management, order processing, and admin controls. The database used is SQLite for simplicity and local development.

---

## Features

- **User Authentication**: Custom user model with registration, login, and user panel.
- **Product Management**: Categories, brands, product details, tags, galleries, and product visit tracking.
- **Shopping Cart**: Persistent user basket, order summary, and checkout.
- **Order Processing**: Manage orders and payment integration (Zarinpal payment gateway).
- **Admin Panel**: Comprehensive admin interface to manage products, orders, site settings, and users.
- **Articles & Blog**: Article module for publishing articles and blog posts.
- **Contact & Support**: Contact form for user inquiries.
- **Site Customization**: Sliders, banners, footer links, and site settings for marketing and information.
- **Persian (fa-IR) Localization**: Jalali calendar support and localized interface.
- **Responsive Frontend**: Built with modern JavaScript, HTML, and CSS.
- **Email Support**: SMTP configuration for notifications and password recovery.

---

## Main Django Apps

- `home_module`: Homepage and general views
- `product_module`: Product, category, brand, tag, gallery, and visit management
- `order_module`: Orders and order details, payment gateway integration
- `account_module`: User registration, authentication, and profiles
- `user_panel_module`: User dashboard and shopping history
- `admin_panel`: Custom admin interfaces
- `article_module`: Blog/article system
- `contact_module`: Contact forms and email handling
- `site_module`: Site settings, banners, sliders, and footer links
- `polls`: (Presumably for polls/surveys)
- 3rd-party: `django_render_partial`, `sorl.thumbnail`, `jalali_date`, `widget_tweaks`

---

## Getting Started

### Prerequisites

- Python 3.7+
- Django 3.2+
- SQLite (default, comes with Python)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AliMirlohi/django-online_shop.git
    cd django-online_shop
    ```

2. **Install dependencies:**

    *(If you have a `requirements.txt`, use it, else manually install Django and dependencies as discovered in the code)*

    ```bash
    pip install django sorl-thumbnail django-jalali widget-tweaks
    ```

3. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the app:**

    - Main Site: [http://localhost:8000/](http://localhost:8000/)
    - Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Configuration

- **Database**: Defaults to SQLite (`db.sqlite3`). You can change this in `eshop_project/settings.py`.
- **Email**: Set up your SMTP credentials in `eshop_project/settings.py` under the EMAIL settings.
- **Static & Media Files**: Static files in `static/`, uploads in `uploads/` (served as `/medias/`).

---

## Payment Integration

- Uses Zarinpal payment gateway (Iranian payment provider). Update merchant credentials for production usage in `order_module/views.py`.

---

## Localization

- Default language is Persian (`fa-IR`).
- Jalali calendar support via `jalali_date`.

---

## Project Structure

```
eshop_project/           # Django project settings
home_module/             # Homepage views
product_module/          # Product catalog
order_module/            # Orders and checkout
account_module/          # User accounts
user_panel_module/       # User dashboard
admin_panel/             # Custom admin interfaces
article_module/          # Articles/blog
contact_module/          # Contact forms
site_module/             # Site-wide settings, banners, etc.
polls/                   # Polls/surveys
static/                  # Static files (CSS, JS, images)
templates/               # HTML templates
uploads/                 # Uploaded media
```

---

## Development Notes

- **Authentication**: Custom user model (`account_module.User`)
- **Persian support**: Jalali date in admin and UI
- **Banners & Sliders**: Easy site customization for marketing
- **Modular**: Each module is a Django app for easy extension

---


## Author

- [Ali Mirlohi](https://github.com/AliMirlohi)
