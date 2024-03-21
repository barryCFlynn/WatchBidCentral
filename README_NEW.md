# Watch Bid Central

'WatchBidCentral' is an exclusive digital haven tailored for the aficionados of timekeeping, offering a marketplace that celebrates the art and craft of luxury watches. This platform is not just a website; it's a dynamic community for both sellers and buyers to engage in the passionate exchange of exquisite timepieces. From vintage classics to contemporary marvels, WatchBidCentral is dedicated to connecting watch enthusiasts around the globe.

Here, users can craft listings for their cherished watches, bid on a diverse collection from esteemed manufacturers, and immerse in a realm where precision meets elegance. WatchBidCentral prides itself on ensuring a secure, transparent, and straightforward experience, making it the premier destination for acquiring and distributing luxury watches.

Embracing the legacy and innovation of the watchmaking tradition, WatchBidCentral is a confluence of history, artistry, and technology. It's a community where every tick, design, and story behind the watch matters, offering a unique space for enthusiasts to share, discover, and elevate their passion for watches. Join the journey at WatchBidCentral, where every second is a celebration of time's endless dance.

<center> 

![Mockup image](/assets/img/README_images/index.jpg) 

</center>


Developer: [Barry Flynn](https://github.com/barryCFlynn/) <br>
[Live webpage](https://watch-bid-central-95b83adfb641.herokuapp.com/)<br>
[Project Repository](https://github.com/barryCFlynn/WatchBidCentral)<br>


![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=for-the-badge)
![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=for-the-badge)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=for-the-badge)

![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)

---

## Table of Content

- [Project Goals](#project-goals)
    + [User Goals](#user-goals)
    + [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    + [Target Audience](#target-audience)
    + [User Requirements and Expectations](#user-requirements-and-expectations)
    + [User Stories](#user-stories)
      - [Epic 1: User Experience (Visitor)](#epic-1--user-experience--visitor-)
      - [Epic 2: User Engagement and Interaction (Registered User)](#epic-2--user-engagement-and-interaction--registered-user-)
      - [Epic 3: Administration and Content Management (Admin/Content Moderator)](#epic-3--administration-and-content-management--admin-content-moderator-)
- [Database](#database)
    + [Blog Application Database Schema](#blog-application-database-schema)
      - [CultureCategory Table](#culturecategory-table)
      - [UserProfile Table](#userprofile-table)
      - [User Table](#user-table)
      - [Post Table](#post-table)
      - [Comment Table](#comment-table)
- [Design](#design)
    + [Design Choices](#design-choices)
    + [Color](#color)
    + [Fonts](#fonts)
    + [Structure](#structure)
      - [Before User logs in:](#before-user-logs-in-)
      - [After User logged in:](#after-user-logged-in-)
      - [Profile Navigation:](#profile-navigation-)
    + [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks](#frameworks)
    + [Database](#database-1)
    + [Media management platform](#media-management-platform)
    + [Tools](#tools)
    + [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- [Methodology](#methodology)
    + [Agile Project Management with GitHub Projects](#agile-project-management-with-github-projects)
    + [User Stories as GitHub Issues](#user-stories-as-github-issues)
    + [Bug Tracking for Seamless Development](#bug-tracking-for-seamless-development)
    + [Iterative Development Approach](#iterative-development-approach)
    + [Future Backlog and Progress](#future-backlog-and-progress)
- [Features](#features)
    + [Landing Page:](#landing-page-)
    + [Other Pages:](#other-pages-)
    + [User Account Management:](#user-account-management-)
    + [Navigation:](#navigation-)
    + [Future Features](#future-features)
- [Testing](#testing)
- [Bugs](#bugs)
    + [Known bugs](#known-bugs)
    + [Fixed bugs](#fixed-bugs)
- [Deployment](#deployment)
    + [App Deployment](#app-deployment)
    + [Cloudinary](#cloudinary)
    + [Version Control](#version-control)
    + [Forking the Repository:](#forking-the-repository-)
    + [Clone of the Repository:](#clone-of-the-repository-)
- [Credits](#credits)
    + [Media](#media)
    + [Django Documentation:](#django-documentation-)
    + [Bootstrap docs:](#bootstrap-docs-)
    + [Tutorials and YouTube channels:](#tutorials-and-youtube-channels-)
    + [Content](#content)
- [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


---

# Project Goals 

Culture Club is a Django web application that serves as a vibrant community platform for cultural enthusiasts to share and explore diverse cultural content including movies, books, podcasts, and music. The key objectives of the project include:

- To provide a user-friendly interface where users can easily share and discover cultural experiences.
- To foster a community of cultural exchange, where users can engage in discussions, express their opinions, and connect with like-minded individuals.
- To offer a personal space for users to curate and display their cultural interests and recommendations.
- To ensure secure and straightforward user registration, authentication, and profile management.
- To allow users to actively participate by creating content, and liking and commenting on posts.

### User Goals

- To discover and engage with content that aligns with their cultural interests.
- To find a platform that allows them to express their own cultural narratives and experiences.
- To join a community that values and fosters cultural diversity and exchange.

### Site Owner Goals

- To build a community-driven platform that encourages user interaction and content creation.
- To maintain a high standard of user experience with seamless navigation and responsive design.
- To ensure the website is a safe and welcoming space for all users to share their cultural passions.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# User Experience

### Target Audience

Culture Club is designed for the following target audience:

- Individuals passionate about various cultural domains who are looking for a space to explore and share content.
- Users seeking a platform to keep track of their cultural experiences and get recommendations from a like-minded community.
- Cultural content creators looking for an outlet to publish their work and engage with an audience.

### User Requirements and Expectations

When using Culture Club, users can expect the following features and characteristics to fulfill their needs:

- An aesthetically pleasing and intuitive interface that provides ease of navigation and content discovery.
- A secure registration and login process, ensuring user data protection and privacy.
- Interactive features such as the ability to like, comment, and create posts that facilitate community engagement.
- A personalized user profile where they can showcase their favorite cultural elements and manage their contributions.
- Access to a diverse range of cultural content and the opportunity to contribute their own insights and reviews.


### User Stories

User stories and tasks were put int o four 'epics' and are organized into four distinct sprints (milestones) to establish a well-defined work structure. You can access the details of these milestones by clicking [here](https://github.com/DebbieBergstrom/Culture-Club/milestones?state=closed), which will take you to the milestone overview.

### Epic 1: User Authentication & Profile Management
This epic focuses on user account management, including registration, login/logout, and personal profile customization.
- [User Account Registration (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/2)
- [Easy Login from Landing Page (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/20)
- [Log out of User account (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/3)
- [Create, Update & Delete User Profile (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/4)
- [Favorite Lists in Personal Bio (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/5)
- [Password Reset (WON'T HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/43)

### Epic 2: Blog Interaction & Content Management
This epic deals with the core functionalities of the blog, such as creating, reading, editing, and deleting posts, as well as interacting with posts through comments and likes.
- [User Create, Edit & Delete Blog Posts (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/7)
- [Comment Blog Posts (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/8)
- [Like/ Unlike Blog Posts (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/9)
- [View Other Users' Profiles (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/10)
- [See Post Overview (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/11)
- [Read Full Post Detail (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/12)
- [Bookmark Blog Posts (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/29)
- [Follow Other Users (WON'T HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/30)
- [Receive Validating Messages (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/37)

### Epic 3: Administration & Analytics
This epic encompasses administrative control over the site, including user account management and content moderation, as well as tracking user engagement.
- [Admin - Full Control Over User Accounts (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/13)
- [Admin - Review and Edit User-Submitted Blog Posts (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/14)
- [Admin - Manage and Categorize Blog Posts (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/15)
- [Admin - Track User Engagement and Analytics (WON'T HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/16)

### Epic 4: User Experience & Accessibility
This epic is focused on the overall user experience on the site, such as the appearance of the homepage, ease of navigation, and accessibility of information.
- [Visually Appealing Landing Page (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/17)
- [Navigate to About Us (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/18)
- [Navigate to Join the Club Section (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/19)
- [Navigate through a well designed website (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/33)
- [Site pagination for easy navigation (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/32)
- [Receive Page Error Messages (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/42)

<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Database
When creating the database structure schema for this project, I utilized the [dbdiagram.io](https://dbdiagram.io/) website. This online tool allowed me to visually design and document the database schema, making it easier to plan and implement the database for the blog application.

<center> 

![Database Schema image](/docs/readme/database_schema.png) 

</center>

## Database Schema Summary

### `User` Table
- Represents the basic user information according to Django's built-in User model.
- Fields: `username`, `email`, `password`.

### `UserProfile` Table
- Extends the User model to store additional information and personal preferences.
- Fields: `user_profile_id`, `user_id`, `profile_image`, `bio`, `country`, `top_movies`, `top_series`, `top_music_albums`, `top_books`, `top_podcasts`, `top_miscellaneous`.

### `MediaCategory` Table
- Stores the different categories for media types that users can select when creating a blog post.
- Fields: `media_category_id`, `media_name`.

### `BlogPost` Table
- Stores individual blog posts written by users, with details about the media being discussed.
- Fields: `blogpost_id`, `blog_title`, `slug`, `author_id`, `created_on`, `updated_on`, `content`, `excerpt`, `status`, `featured_image`, `media_category_id`, `release_year`, `media_link`, `likes`, `bookmarks`.

### `Comment` Table
- Stores comments made by users on blog posts.
- Fields: `comment_id`, `body`, `created_on`, `approved`, `blogpost_id`, `user_id`.

This database schema lays out the structure for the Culture Club application, facilitating user interaction with blog posts, personalization of user profiles, categorization of posts by media type, and community engagement through comments, likes, and bookmarks.


<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Design

The design of Culture Club is crafted with a blend of nostalgia and modernity, reflecting the essence of cultural appreciation that spans generations. The choices in colors, fonts, and layout are intended to evoke a sense of familiarity and warmth, welcoming users to a community where culture in all its forms is cherished and discussed.

### Design Choices

Design choices were made with the intention of creating an inviting and user-friendly interface that also resonates with the theme of cultural nostalgia. The darker theme breaks from the contemporary trend of minimalistic and bright designs, offering a unique visual experience that aligns with the interests of culture enthusiasts who often have a fondness for timeless classics in movies, music, books, and more.

### Color

In creating balanced interfaces that are both visually appealing and functional, we carefully selected a color palette that complements the overall theme of the site.

![Color Palette image](docs/readme/colorpalette.png)

**Dominant:**

The choice of 'Gunmetal' Green, represented by #012326, as the dominant color, reflects the depth and richness of cultural history. This dark green hue sets a strong foundation for the site's design, providing a serene and focused backdrop for content exploration.

**Secondary:**

'Munsell Blue', represented by #0794A7, serves as the secondary color. This choice is a nod to the vibrancy and dynamism of the cultural sphere. It not only complements the darker green but also adds a splash of energy and modern flair to the design.

**Accent:**

Our accent color is a carefully chosen shade of 'Burnt Orange', represented by #B9581B. This color provides a striking contrast to the greens and blue, drawing attention to important elements like buttons and calls to action. It brings a sense of excitement and highlights the interactive aspects of the site.

**Other colors:**
A softer shade of yellow 'Flax, represented by #E2DA83, used for inline links and smaller elements, adds a subtle yet effective highlight, ensuring that navigation elements are easily identifiable.

Instead of regular white text color, a bit more "greenbluish" shade of white called 'Light Cyan'represented by #CBEAF1, were chosen to blend well with all colors, yet still have great contrast. 

### Fonts

For the Culture Club site, we selected fonts that harmonize with our theme of blending the nostalgic with the contemporary. The H1 headers feature a distinctive font, 'Russo One', that resonates with the nostalgic 80-90's aspect of the site, while the classic Roboto font is used for the body text, ensuring readability and a modern touch. This combination of fonts not only enhances the aesthetic appeal but also contributes to an enjoyable user experience.

### Structure

The Culture Club website is designed with a user-friendly structure, ensuring seamless navigation and easy access to the website's diverse content about movies, music, books, podcasts, and more. Below is an overview of the website's structure:

#### Before User Logs In:

- **Landing Page with Sign In Form:** Upon arrival, users are greeted by a visually engaging landing page that doubles as a login portal. The page showcases a large, thematic image representing the site's focus on various cultural elements. Adjacent to the image is the login form, enabling existing users to quickly access their accounts. For newcomers, convenient links to the 'About Us' page and 'Sign Up' form are prominently displayed, inviting them to join the community.

- **About Us:** This page provides insightful information about the Culture Club, its mission, and what new members can expect upon joining. It serves as an introduction to the site's ethos and community spirit.

- **Sign Up:** A welcoming space for new users, the 'Join Us' page offers an easy and straightforward sign-up process, encouraging cultural enthusiasts to become a part of the vibrant Culture Club community.

#### After User Logs In:

Post-login, users gain access to a range of interactive and personalized features:

- **Home Page (Inside the Culture Club):** The heart of the site, the home page presents the latest posts. Users can enjoy a broad overview of all posts or filter content by categories using the category selection buttons. Each post is displayed as an engaging card, featuring a clickable image (to the full post view), the title, a brief excerpt, author's name, and the number of likes.

- **Full Blog Post View:** Each blog post can be viewed in its entirety on a dedicated page. This full view not only presents the complete content of the post, including images and detailed text, but also fosters user interaction and community engagement. Below each post, a comment section allows users to share their thoughts, engage in discussions, and connect with others. The author's name is linked to their user profile. Similarly, every user who comments has a clickable name that directs to their profile, enabling a deeper exploration of the community and fostering connections among users with similar interests.

- **Create New Post:** A creative space where users can share their cultural insights. This form allows for the inclusion of relevant images, titles, excerpts, detailed blog content, release year (for movies, for instance), media category, and reference URLs. New posts, once published, are prominently displayed on the home page.

- **My Posts:** A personalized collection of the user's blog posts. This page not only showcases their contributions but also offers 'Edit' and 'Delete' options for each post, giving users full control over their content.

- **Bookmarked:** A curated list of the user's bookmarked posts, allowing for quick access to favorite articles and discussions. Users can easily bookmark or remove bookmarks as they navigate through the site.

#### Profile Navigation:

Accessing the profile icon in the navigation bar opens up more user-specific features:

- **Profile Page:** A personal showcase featuring the user's profile picture, bio, country of origin, and their 'Top Selections' in various cultural categories like 'Movies', 'Series', 'Music Albums', etc. This page is a window into each user's unique tastes and interests.

- **Edit Profile Page:** Users can update their profile details, ensuring their personal page reflects their evolving preferences and experiences.

- **Manage Account:** A crucial feature for account management, this page allows users to delete their account. It includes clear warnings about the permanence of this action and requires confirmation to proceed, ensuring users make informed decisions.

- **Log Out:** A simple yet secure logout process. Users are prompted to confirm their intention to log out, safeguarding their account access. Once logged out they get redirected to the log in landing page. 


### Wireframes
The wireframes serve as a visual blueprint for the application. Click on each page to view the wireframe.

<details><summary>Landing page</summary>
<img src="docs//readme/wireframes/landig_spage_signin.png">
</details>
<details><summary>About us</summary>
<img src="docs/readme/wireframes/about_us.png">
</details>
<details><summary>Join the Club</summary>
<img src="docs/readme/wireframes/create_account.png">
</details>
<details><summary>Home Page - Post Overview</summary>
<img src="docs/readme/wireframes/home_post_overview.png">
</details>
<details><summary>Full Post View</summary>
<img src="docs/readme/wireframes/full_post_view.png">
</details>
<details><summary>Create New Post</summary>
<img src="docs/readme/wireframes/create_new_post.png">
</details>
<details><summary>Edit / Update Post</summary>
<img src="docs/readme/wireframes/edit_update_post.png">
</details>
<details><summary>My Posts / Bookmarked</summary>
<img src="docs/readme/wireframes/my_posts_bookmarked.png">
</details>
<details><summary>Manage Account</summary>
<img src="docs/readme/wireframes/manage_account.png">
</details>
<details><summary>My Profile</summary>
<img src="docs/readme/wireframes/my_profile.png">
</details>
<details><summary>User Profile</summary>
<img src="docs/readme/wireframes/user_profile.png">
</details>


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Technologies Used

### Languages
- HTML
- CSS
- Python
- JavaScript

### Frameworks
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design, used for building the Culture Club web application.
- **Crispy Forms**: A Django package that simplifies form layout and styling, making forms more efficient and customizable.
- **Bootstrap v5.0**: The latest version of the popular CSS framework, used for creating responsive and visually appealing user interfaces.

### Database
- **ElephantSQL**: A cloud-hosted PostgreSQL database service, offering a reliable and scalable storage solution for the application's data.

### Media Management Platform
- **Cloudinary**: A cloud-based platform for media upload, storage, optimization, and delivery, used for managing images in the Culture Club project.

### Tools
- **Git**: A version control system for tracking changes in source code during software development.
- **GitHub**: A platform for hosting and managing Git repositories, enabling collaboration and version control for the project's codebase.
- **Gitpod**: A cloud-based IDE that provides a consistent and pre-configured development environment for the Culture Club project.
- **Heroku**: A cloud application platform used for deploying and hosting the Culture Club web application.
- **Adobe Photoshop**: A graphic design software used for editing and refining images for the website.
- **DB Diagram**: A tool for visualizing and creating database schemas, used for planning the database structure of Culture Club.
- **Google Fonts**: A library of free, open-source fonts, used to enhance typography on the website.
- **Font Awesome**: A library of icons and social logos, used for adding graphical elements to the Culture Club interface.
- **DALL-E**: An AI generative image tool utilized for creating unique images for the landing page and blog post placeholder.
- **Balsamiq**: A wireframing tool used for sketching and visualizing the layout and structure of the web project.


### Supporting Libraries and Packages

- `asgiref==3.7.2`: foundational package for Django to support asynchronous web protocols like WebSockets.
- `cloudinary==1.37.0`: integration library for Cloudinary - cloud service for storing and managing media files and assets.
- `dj-database-url==0.5.0`: utility to help you configure your Django application's database from the DATABASE_URL environment variable.
- `dj3-cloudinary-storage==0.0.6`: Django storage backend for Cloudinary to handle media and static files.
- `Django==3.2.23`: Django web framework; the core framework for the web application.
- `django-allauth==0.59.0`: integrated set of Django applications addressing authentication, registration, account management, and third-party (social) account authentication.
- `django-crispy-forms==1.14.0`: Django app that provides a way to render Django forms in a DRY, configurable, and reusable way.
- `django-summernote==0.8.20.0`: Django app that integrates the Summernote WYSIWYG editor for text fields.
- `gunicorn==21.2.0`: Python WSGI HTTP Server for UNIX - robust and performant server to serve the Django application.
- `oauthlib==3.2.2`: generic, spec-compliant implementation of OAuth for use as a foundation for OAuth consumers and providers.
- `psycopg2==2.9.9`: PostgreSQL database adapter for Python, a prerequisite for using PostgreSQL with Django.
- `PyJWT==2.8.0`: Python library to encode and decode JSON Web Tokens (JWT), often used in authentication mechanisms.
- `python3-openid==3.2.0`: Python 3 port of the Python OpenID library, used for OpenID authentication.
- `pytz==2023.3.post1`: Python library that allows accurate and cross-platform timezone calculations.
- `requests-oauthlib==1.3.1`: An OAuthlib authentication support for Requests, which allows you to use OAuth to authenticate with APIs.
- `sqlparse==0.4.4`: non-validating SQL parser for Python, useful for parsing and splitting SQL statements.
- `urllib3==1.26.15`: powerful HTTP client for Python. Used by Requests internally.




<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Methodology

The Culture Club project follows a methodology inspired by agile principles, fostering collaboration, flexibility, and gradual development. The outlined approach has guided the project's evolution:

### Agile Project Management with GitHub Projects
To streamline project management, GitHub Projects is employed as a central hub. User stories and tasks are structured as GitHub issues, creating an organized workflow. The GitHub project board serves as a visual representation, tracking progress effectively.

### User Stories as GitHub Issues
Transforming user stories into GitHub issues captures user-centric functionalities. These issues interlink with respective user stories, simplifying access to criteria, tasks, and comments.

### Bug Tracking for Seamless Development
Bugs uncovered during development are documented as GitHub issues, offering insights into each bug's characteristics, impact, and reproduction steps. By hyperlinking these issues in README.md, users can stay updated on bug resolutions and contribute insights.

### Iterative Development Approach
The Culture Club project adheres to an iterative development approach, facilitating continuous enhancements within a predefined timeline. Despite its condensed schedule, the project accommodates future iterations and expansions.

### Future Backlog and Progress
The project board efficiently manages user stories, with the "Not started" column representing upcoming iterations. This backlog previews user stories set for subsequent development phases.

Emphasizing that the project timeline is expedited, the iterative approach maintains adaptability, enabling ongoing refinements and improvements aligned with evolving user needs.

**Labels and User Story Distribution (MoSCoW):**

### Must-Have:
- User Account Registration [#2](https://github.com/DebbieBergstrom/Culture-Club/issues/2)
- Log In and Out of User Account [#3](https://github.com/DebbieBergstrom/Culture-Club/issues/3)
- Edit User Bio and Profile Picture [#4](https://github.com/DebbieBergstrom/Culture-Club/issues/4)
- User Create & Edit Blog Posts [#7](https://github.com/DebbieBergstrom/Culture-Club/issues/7)
- Comment Blog Posts + Edit [#8](https://github.com/DebbieBergstrom/Culture-Club/issues/8)
- Read Full Post Detail [#12](https://github.com/DebbieBergstrom/Culture-Club/issues/12)
- Admin - Full Control Over User Accounts [#13](https://github.com/DebbieBergstrom/Culture-Club/issues/13)
- Navigate to Join the Club Section [#19](https://github.com/DebbieBergstrom/Culture-Club/issues/19)
- Easy Login from Landing Page [#20](https://github.com/DebbieBergstrom/Culture-Club/issues/20)
- Navigate through a well designed website [#33](https://github.com/DebbieBergstrom/Culture-Club/issues/33)

### Should-Have:
- Like/ Unlike Blog Posts [#9](https://github.com/DebbieBergstrom/Culture-Club/issues/9)
- View Other Users' Profiles [#10](https://github.com/DebbieBergstrom/Culture-Club/issues/10)
- See Post Overview [#11](https://github.com/DebbieBergstrom/Culture-Club/issues/11)
- Admin - Review and Edit User-Submitted Blog Posts [#14](https://github.com/DebbieBergstrom/Culture-Club/issues/14)
- Visually Appealing Landing Page [#17](https://github.com/DebbieBergstrom/Culture-Club/issues/17)
- Navigate to About Us [#18](https://github.com/DebbieBergstrom/Culture-Club/issues/18)
- Site pagination for easy navigation [#32](https://github.com/DebbieBergstrom/Culture-Club/issues/32)
- Receive Validating Messages [#37](https://github.com/DebbieBergstrom/Culture-Club/issues/32)
- Receive Page Error Messages [#42](https://github.com/DebbieBergstrom/Culture-Club/issues/32)

### Could-Have:
- Favourite Lists in Personal Bio [#5](https://github.com/DebbieBergstrom/Culture-Club/issues/5)
- Bookmark Blog Posts [#29](https://github.com/DebbieBergstrom/Culture-Club/issues/29)
- Admin - Manage and Categorize Blog Posts [#15](https://github.com/DebbieBergstrom/Culture-Club/issues/15)

### Won't-Have:
- Password Reset [#43](https://github.com/DebbieBergstrom/Culture-Club/issues/43)
- Follow Other Users [#30](https://github.com/DebbieBergstrom/Culture-Club/issues/30)
- Admin - Track User Engagement and Analytics [#16](https://github.com/DebbieBergstrom/Culture-Club/issues/16)

For a comprehensive view of the project's trajectory, user stories, and bug tracking, explore the [Kanban board](https://github.com/users/DebbieBergstrom/projects/4/views/1).
<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Features
### Login Landing Page:
- Description: The landing page provides a welcoming first impression with easy access to login and information about the site. The navigation bar and footer is visible on every page.
<details><summary>See Screenshot **Landingpage, large**</summary><img src="docs/features/login_landing_page.png"></details>
<details><summary>See Screenshot **Landingpage, mobile**</summary><img src="docs/features/login_landing_page_sm.png"></details>
<details><summary>See Screenshot **Navigation bar**</summary><img src="docs/features/navbar_logged_out.png"></details>
<details><summary>See Screenshot **Footer**</summary><img src="docs/features/footer.png"></details>

### About Us:
- Description: A detailed section introducing users to the concept and team behind Culture Club. 
<details><summary>See Screenshot **About us, large**</summary><img src="docs/features/about_us.png"></details>
<details><summary>See Screenshot **About us, mobile**</summary><img src="docs/features/about_us_sm.png"></details>

### Join the Club/ Sign Up:
- Description: A straightforward sign-up page enabling new users to join the community.
<details><summary>See Screenshot **Sign Up, large**</summary><img src="docs/features/sign_up.png"></details>
<details><summary>See Screenshot **Sign Up, mobile**</summary><img src="docs/features/sign_up_sm.png"></details>

### Home / Index Blog Post view (Logged in User):
- A dynamic homepage showcasing the latest blog posts, with user-friendly navigation and category filtering. When user is logged in the navigation bar has more links. Site pagination is seen at the bottom to see more pages of posts. 
<details><summary>See Screenshot **Login, success message**</summary><img src="docs/features/msg_signed_in.png"></details>
<details><summary>See Screenshot **Home Page, large**</summary><img src="docs/features/index.png"></details>
<details><summary>See Screenshot **Home Page, mobile**</summary><img src="docs/features/index_sm.png"></details>
<details><summary>See Screenshot **Navbar, logged in user**</summary><img src="docs/features/navbar_logged_in.png"></details>
<details><summary>See Screenshot **Site pagination 'next'**</summary><img src="docs/test.md/userstories/us_pagination_next.png"></details>
<details><summary>See Screenshot **Site pagination 'prev'**</summary><img src="docs/test.md/userstories/us_pagination_prev.png"></details>
<details><summary>See Screenshot **Category active button**</summary><img src="docs/features/category_active_button.png"></details>

### Read Full Post:
- Description: An immersive page for reading entire blog posts, complete with like, bookmark, and comment functionalities.
<details><summary>See Screenshot **Read Full Post, large**</summary><img src="docs/features/create_new_post.png"></details>
<details><summary>See Screenshot **Read FullPost, mobile**</summary><img src="docs/features/create_new_post_sm.png"></details>
<details><summary>See Screenshot **Like Post**</summary><img src="docs/test.md/userstories/us_like_post.png"></details>
<details><summary>See Screenshot **Unlike Post**</summary><img src="docs/test.md/userstories/us_unliked.png"></details>
<details><summary>See Screenshot **Bookmark Post**</summary><img src="docs/test.md/userstories/us_bookmarked.png"></details>
<details><summary>See Screenshot **Unbookmark Post**</summary><img src="docs/test.md/userstories/us_unbookmarked.png"></details>
<details><summary>See Screenshot **Comment Post**</summary><img src="docs/features/us_blogpost_comment.png"></details>

### Create New Post:
- Description: A user-friendly interface for creating new blog posts, with fields for title, content, images, and more. Validating message displays when post is successfully created.
<details><summary>See Screenshot **Create New Post, large**</summary><img src="docs/features/create_new_post.png"></details>
<details><summary>See Screenshot **Create New Post, mobile**</summary><img src="docs/features/create_new_post_sm.png"></details>
<details><summary>See Screenshot **Create New Post, success message**</summary><img src="docs/features/msg_post_created.png"></details>

### Edit Post:
- Description: Allows users to make changes to their existing blog posts, with an intuitive editing interface. Validating message displays when post is successfully updated.
<details><summary>See Screenshot **Edit Post, large**</summary><img src="docs/test.md/userstories/us_edit_post.png"></details>
<details><summary>See Screenshot **Edit Post, mobile**</summary><img src="docs/features/edit_post_sm.png"></details>
<details><summary>See Screenshot **Edit Post, success message**</summary><img src="docs/features/msg_post_updated.png"></details>

### Delete Post:
- Description: A confirmation page for users to delete their blog posts, ensuring mindful content management. Validating message displays when post is successfully deleted.
<details><summary>See Screenshot **Delete Post, large**</summary><img src="docs/features/delete_post.png"></details>
<details><summary>See Screenshot **Delete Post, mobile**</summary><img src="docs/features/delete_post_sm.png"></details>
<details><summary>See Screenshot **Delete Post, success message**</summary><img src="docs/features/msg_post_deleted.png"></details>

### My Posts:
- Description: A dedicated space for users to view and manage all their published blog posts.
<details><summary>See Screenshot **My Posts, large**</summary><img src="docs/features/my_posts.png"></details>
<details><summary>See Screenshot **My Posts, mobile**</summary><img src="docs/features/my_posts_sm.png"></details>

### Bookmarked page:
- Description: A special page for users to view all their bookmarked blog posts for easy access. 
<details><summary>See Screenshot **Bookmarked, large**</summary><img src="docs/features/bookmarked.png"></details>
<details><summary>See Screenshot **Bookmarked, mobile**</summary><img src="docs/features/bookmarked_sm.png"></details>

### User Profiles:
- Description: A comprehensive profile page displaying user information, top picks in various media categories and profile image. If it's the logged in users own profile, the links to 'Edit Profile' and 'Manage Account' is visible.
<details><summary>See Screenshot **Owner User Profile with uploaded image, large**</summary><img src="docs/test.md/userstories/us_own_user_profile.png"></details>
<details><summary>See Screenshot **Owner User Profile with placeholder image, mobile**</summary><img src="docs/features/user_profile_placeholderimg_sm.png"></details>
<details><summary>See Screenshot **Other User Profile without edit/manage links**</summary><img src="docs/test.md/userstories/us_other_user.png"></details>


### Edit Profile:
-  An edit profile page allowing users to update their personal information and preferences. Validating message displays when profile is successfully updated.
<details><summary>See Screenshot **Edit Profile, placeholder image default, large**</summary><img src="docs/features/edit_profile_placeholder.png"></details>
<details><summary>See Screenshot **Edit Profile, placeholder image default, mobile**</summary><img src="docs/features/edit_profile__placeholder_ sm.png"></details>
<details><summary>See Screenshot **Edit Profile, success message**</summary><img src="docs/features/msg_profile_updated.png"></details>


### Manage Account / Delete Profile:
- Provides users with account management option to be able to delete their account. When confirmed 'Delete Account' button is clicked there's an extra layer of confirmation for security when a popup warning ask for one more confirm.
<details><summary>See Screenshot **Manage Account, large**</summary><img src="docs/features/manage_account.png"></details>
<details><summary>See Screenshot **Manage Account, mobile**</summary><img src="docs/features/manage_account_sm.png"></details>
<details><summary>See Screenshot **Manage Account, extra on click Delete Warning**</summary><img src="docs/features/onclick-delete_warning.png"></details>

### Logout:
- A simple and secure logout process, ensuring users can safely exit their account. Validating message displays when user is successfully logged out.
<details><summary>See Screenshot **Log out, large**</summary><img src="docs/features/log_out.png"></details>
<details><summary>See Screenshot **Log out, mobile**</summary><img src="docs/features/log_out_sm.png"></details>
<details><summary>See Screenshot **Log out, success message**</summary><img src="docs/features/msg_signed_out.png"></details>


### Future Features
Here are some exciting features that I would like to add to the Culture Club in the future:

| Feature | Description |
| --- | --- |
| **Forgot Password Functionality** | Implement the ability for users to retrieve a new password if forgotten. [User Story #43](https://github.com/DebbieBergstrom/Culture-Club/issues/43) |
| **User Engagement and Analytics Tracking for Admin** | Enhance admin capabilities to track user engagement and analytics for improved user experience. [User Story #16](https://github.com/DebbieBergstrom/Culture-Club/issues/16) |
| **User Follow Functionality** | Allow users to follow other users to stay updated on their activities and posts. [User Story #30](https://github.com/DebbieBergstrom/Culture-Club/issues/30) |
| **Comment Editing and Deletion** | Enable users to edit and delete their comments for better content control. |
| **Nested Comment Fields** | Implement nested comments for a more organized and engaging discussion interface. |
| **Improved Image Resizing** | Enhance image uploading experience with better resizing options and user guidance on image handling. |
| **File Size Restrictions for Images** | Implement restrictions on image file size or functions to automatically downscale images for optimal performance. |
| **Social Account Login Integration** | Enable login through social media accounts for a more seamless user experience. |
| **User's Blog Posts on Profile** | Display a list of a user's blog posts on their profile for easier access by others. |
| **User's social media links in profile** | Optionally the user can let other users know their presence on other social platforms. |
| **Additional Back-Buttons** | Improve site navigation with more back-buttons for seamless user interaction. |
| **Contact Form for Site Feedback** | Introduce a contact form for users to report bugs or inappropriate behavior within the community. |
| **Community Guidelines and Policy Page** | Establish a page outlining community rules and policies, including respect and decorum among users. |
| **Search Functions** | Add a search function to allow users to find specific blog posts and other users easily. |
| **Design Improvements** | Continual enhancements in design, including better headings and text sizing for various screen sizes. |
|  |  |


<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Testing

The Culture Club website went through a comprehensive testing process to guarantee its functionality, accessibility, and performance. This included checking the code, such as code validation, accessibility assessment, performance testing, cross-device testing, verification of browser compatibility, assessment of user stories, and the integration of user feedback to enhance the overall user experience.

All testing was carried out and documented in [testing.md](https://github.com/DebbieBergstrom/Culture-Club/blob/main/TESTING.md). 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Bugs
The bug description section have been linked with the bug issues in my documentation for better visibility. The issue numbers are clickable to get a more comprehensive bug report.

### Known bugs ❌ 

| Bug Description | Bug Issue Link |
| --- | --- |
| Masthead image not scaling properly See screenshot here: <details><summary>Screenshot showing bug result</summary>![Result](docs/test.md/test_image_max_height.png)</details> | More information &rarr; [#46](https://github.com/DebbieBergstrom/Culture-Club/issues/46) |
| No linebreak if User Name too long <details><summary>Screenshot showing bug</summary>![Result](docs/test.md/test_chars_overflow_userprofile.png)</details> | More information &rarr; [#47](https://github.com/DebbieBergstrom/Culture-Club/issues/47) |


### Fixed bugs ✅

| Bug Description | Bug Issue Link |
| --- | --- |
| Placeholder image doesn't show in Profile | More information &rarr; [#39](https://github.com/DebbieBergstrom/Culture-Club/issues/39) |
| Post default image is not displayed | More information &rarr; [#41](https://github.com/DebbieBergstrom/Culture-Club/issues/41) |
| Wrongfully landing page direction | More information &rarr; [#36](https://github.com/DebbieBergstrom/Culture-Club/issues/36) |
| Index file does not render | More information &rarr; [#34](https://github.com/DebbieBergstrom/Culture-Club/issues/34) |
| Author link in post detail not clickable | More information &rarr; [#38](https://github.com/DebbieBergstrom/Culture-Club/issues/38) |
| 'Forgot your password' link can't be removed | More information &rarr; [#44](https://github.com/DebbieBergstrom/Culture-Club/issues/44) |
| Summernote field overflows parent container | More information &rarr; [#45](https://github.com/DebbieBergstrom/Culture-Club/issues/45) |



<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Deployment

### App Deployment
For deploying Your app, Heroku is used. Follow these steps:

 **Create a New App:**
   - Create a new app on Heroku dashboard.

 **Configure Settings:**
   - Navigate to "Settings" in new app.

 **Config Vars Setup:**
   - In "Config Vars," add `PORT` as the key and `8000` as its value.

 **Add PostgreSQL Database:**
   - Choose PostgreSQL as database.

        Example "ElephantSQL" was used in this project

 **Configure DATABASE_URL:**
   - In "Config Vars," add `DATABASE_URL` and copy the URL from PostgreSQL dashboard.

     Note: If using ElephantSQL as PostgreSQL provider, you can use the URL provided by ElephantSQL.

 **Environment Variable Setup:**
   - Create a new file in workspace called `env.py`.
   - Import the `os` library and set the environment variable for `DATABASE_URL` to the Heroku address (or ElephantSQL URL)
   - Add a secret key using `os.environ["SECRET_KEY"] = "your secret key here"`.

 **Heroku Config Vars:**
   - Add the secret key to the Heroku app's config vars in the settings.

 **Django Settings:**
   - In `settings.py` of Django app, import `Path` from `pathlib`, `os`, and `dj_database_url`.
   - Add `if os.path.isfile("env.py"): import env` to the file.
   - Replace the SECRET_KEY with `SECRET_KEY = os.environ.get('SECRET_KEY')`.
   - Replace the database section with `DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`.

 **Migrate Models:**
   - In workspace terminal, migrate the models to the new database connection.

### Cloudinary
To integrate Cloudinary into project, follow these steps:

 **Cloudinary Account:**
   - Log in to Cloudinary account or create one.

 **Copy CLOUDINARY_URL:**
   - Copy `CLOUDINARY_URL`.

 **Environment Variable Setup:**
   - In `env.py`, add `os.environ["CLOUDINARY_URL"] = "add cloudinary_url here"`.

 **Heroku Config Vars:**
   - In Heroku settings, add `CLOUDINARY_URL` to config vars.

 **Django Settings:**
   - In `INSTALLED_APPS`, add `cloudinary_storage`, `Django.contrib.staticfiles`, and `cloudinary` in this order.
   - Configure static file settings in `settings.py`: URL, storage path, directory path, root path, media URL, and default file storage.

 **Templates Directory Link:**
   - Link the file to the templates directory in Heroku with `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`.

 **Change Templates Directory:**
   - Change the templates directory to `TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]`.

 **Additional Folders:**
   - Create three new folders: `media`, `static`, and `templates`.

 **Procfile Creation:**
   - Create a `Procfile`.
   - Add the following line inside the Procfile: `web: gunicorn project_name_here.wsgi`.

 **Push Changes:**
    - Push all changes to GitHub.

 **Manual Deployment:**
    - In the Heroku deployment tab, deploy to Heroku manually the first time and closely monitor the process.
    - Once successful, set up automatic deployments.

### Version Control
To manage version control and push code to the main repository on GitHub using GitPod, follow these steps:

 **Add Changes:**
   - In the GitPod terminal, use the command `git add .` to stage changes.

 **Commit Changes:**
   - Commit changes with a descriptive comment using the command:
     ```
     git commit -m "Push comment here"
     ```

 **Push to GitHub:**
   - Push the updates to the repository on GitHub with the command:
     ```
     git push
     ```

 **Migrate Models:**
    - In the terminal, migrate the models to the new database connection.

### Forking the Repository:

By forking the GitHub Repository, can create a copy of the original repository without affecting the original. Follow these steps:

 **GitHub Account Setup:**
   - Log into GitHub account or create one if you don't have one.

 **Locate the Repository:**
   - Find the repository at https://github.com/DebbieBergstrom/Culture-Club.

 **Fork the Repository:**
   - At the top right of the repository page, click "Fork" to create a copy in your own GitHub repository.

### Clone of the Repository:

Creating a clone allows you to have a local copy of the project. Follow these steps:

 **Repository URL:**
   - Navigate to https://github.com/DebbieBergstrom/Culture-Club.
   - Click the green "Code" button at the top right.

 **Clone the Repository:**
   - Select the "Clone by HTTPS" option and copy the provided URL to the clipboard.

 **Terminal and Git:**
   - Open your code editor or terminal and navigate to the directory where you want to clone the repository.
   - Run `git clone` followed by the copied URL.
   - Press enter, and Git will clone the repository to your local machine.


To fork the repository, follow these steps:

1. Go to the GitHub repository.
2. Click on the Fork button in the upper right-hand corner.
3. Wait for the forking process to complete. Once done, you will have a copy of the repository in your GitHub account.

To clone the repository, follow these steps:

1. Go to the GitHub repository.
2. Locate the Code button above the list of files and click it.
3. Select your preferred method for cloning: HTTPS, SSH, or GitHub CLI, and click the copy button to copy the repository URL to your clipboard.
4. Open Git Bash (or your preferred terminal).
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type the command `git clone` followed by the URL you copied in step 3. The command should look like this: `git clone https://github.com/DebbieBergstrom/Culture-Club`.
7. Press Enter to create your local clone.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Credits
### Here's a collection of sites that were helpful in creating this website:

### Django Documentation:
The official Django documentation with guidance on models, forms, templates, and various aspects of Django development.

- [Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Validators](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)
- [DeleteView](https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/)
- [Mixins & Class based Views](https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/)
- [Authentication System](https://docs.djangoproject.com/en/3.2/topics/auth/default/)
- [URL patterns](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
- [Form Widgets](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/)
- [Messages](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
- [Automated testing](https://docs.djangoproject.com/en/5.0/topics/testing/overview/)

### Bootstrap docs:
- [Increase knowledge of Bootstrap framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

### W3 Schools:
- [Overrite Bootstraps css variables](https://www.w3schools.com/css/css_important.asp)
- [Refresh knowledge of JS addEventListener](https://www.w3schools.com/jsref/met_element_addeventlistener.asp)
- [Explaining truncate word function](https://www.w3schools.com/django/ref_filters_truncatewords.php)

### Geeksforgeeks: 
- [Using Crispy Form](https://www.geeksforgeeks.org/styling-django-forms-with-django-crispy-forms/)

### StackOverflow: 
- [About Django Messages](https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit)
- [About Django Sort by Filter](https://stackoverflow.com/questions/72117712/django-filter-by-category)
- [About Django Form Widgets](https://stackoverflow.com/questions/68736684/modify-django-model-form-field-with-widget)

### Tutorials and YouTube channels:
- [How to Create User Profile](https://www.youtube.com/watch?v=FdVuKt_iuSI)

### Other sites:
- [Styling Crispy forms](https://blog.appseed.us/django-forms-styling-with-bootstrap/)
- [Organize Imports](https://peps.python.org/pep-0008/)
- [Generate Slugs](https://www.kodnito.com/posts/slugify-urls-django/)
- [How to override default django templates](https://www.makeuseof.com/override-default-templates-django-allauth/)
- [Automated testing tutorial](https://www.youtube.com/watch?v=6I_haJimhPY)


- Code Institute, Module 4 & Django Coding Walkthrough material.

### Media
- [Favicon Generator](https://favicon.io/) to create the blue 'C' favicon in the browser tab.
- [Pexels Free Images](https://www.pexels.com/sv-se/) to find some user profile mockup images.
- [Freepik Free Images](https://www.freepik.com/free-photos-vectors/user-profile) to find user profile symbols and default images.

### Content
- Content for the webpage and readme-file was written together with [ChatGPT](https://chat.openai.com/)


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Acknowledgments
 I'd like to give recognition to the ones who have supported me in creating this project:

* [Lauren_Nicole](https://github.com/CluelessBiker), my Code Institute Mentor. I cannot thank her enough for her invaluable guidance and assistance. 

* [Sandra B](https://github.com/SandraBergstrom) and [Kim B](https://github.com/KimBergstroem), who are both great critics and support pillars.

* Code Institute and their helpful staff, especially within our great Slack community.


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---