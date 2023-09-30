from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user manager for the CustomUser model.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create a new user with the given email and password.

        :param email: The email address of the user.
        :param password: The user's password.
        :param extra_fields: Additional fields to save with the user.
        :return: The newly created user object.
        """

        # Check if email is provided
        if not email:
            raise ValueError("The Email field must be set")

        # Normalize the email address (convert to lowercase)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        
        # Set the user's password securely
        user.set_password(password)
        
        # Save the user to the database
        user.save()
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create a new superuser with the given email and password.

        :param email: The email address of the superuser.
        :param password: The superuser's password.
        :param extra_fields: Additional fields to save with the superuser.
        :return: The newly created superuser object.
        """
    
        # Set default values for is_staff and is_superuser if not provided.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Check if is_staff and is_superuser are set to True
        if not extra_fields["is_staff"] or not extra_fields["is_superuser"]:
            raise ValueError("Superuser must have is_staff=True and is_superuser=True.")

        # Create a user with the provided email and password
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model.
    """

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    # Disable the default fields
    first_name = None
    last_name = None
    username = None

    objects = UserManager()  # Use the custom user manager for user creation.

    USERNAME_FIELD = "email"  # Use email as the unique identifier for authentication

    REQUIRED_FIELDS = []  # No additional required fields for user creation

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(" ")[0]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
