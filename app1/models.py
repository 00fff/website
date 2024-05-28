from django.db import models

# Define the Hobbies model
class Hobby(models.Model):
    # A field to store the text describing the hobby, with a maximum length of 200 characters
    text = models.CharField(max_length=200, default="Default Text")
    
    # A field to store the date and time when the hobby was added, automatically set to the current date and time when the object is created
    date_added = models.DateTimeField(auto_now_add=True)
    
    # A string representation of the model object, which returns the text describing the hobby
    class Meta:
        verbose_name_plural = "hobbies"
    
    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text

# Define the HobbyDescription model
class HobbyDescription(models.Model):
    # A field to establish a many-to-one relationship with the Hobbies model, where each hobby description is associated with a single hobby
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    
    # A field to store the description of the hobby
    description = models.TextField()
    
    # A field to store the date and time when the hobby description was added, automatically set to the current date and time when the object is created
    date_added = models.DateTimeField(auto_now_add=True)

    # A string representation of the model object, which includes the text describing the associated hobby
    def __str__(self):
        return f"Description for {self.hobby.text}"
