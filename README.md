# Homework 12
[link to the source](https://skyengpublic.notion.site/12-0fc43954be5343a6a5c47d25db097050)
### Task:
In this homework you will write a small web project for working with messages and forms. You will be able to reuse parts of your solution in coursework. The project should look like this:
![app-example](https://skyengpublic.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa5c64fc4-3731-4c9f-bd16-8c56a78fdbcb%2F2022-02-19_13.40.51.gif?table=block&id=1185f600-c7e2-4273-972c-e95d88c7982f&spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&userId=&cache=v2)
The main page has a search field: when the user enters text and clicks "Search", app returns text contains the substring that the user entered. 
The user can also add a post. The user can enter text and select an image. After sending, the text and image will be shown, the post will be added to the list of posts.
### List of pages:
* `/` – Main page (list of posts)
* `/search/?s=search` – filtered posts page
* `GET /post` – "Add" post page
* `POST /post` – Page shown after adding a post
![pages-example](https://skyengpublic.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb1d5b251-94b1-45e3-98c8-7a0adc677500%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2022-02-18_%D0%B2_17.50.02.png?table=block&id=2cb8a951-14b3-4a5c-8390-370791349821&spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&width=1540&userId=&cache=v2)
## What should you do:
### Step 1:
#### Clone the project from GitHub and explore the HTML templates and folder structure of the project.
[https://github.com/skypro-008/lesson12_project_source_v3](https://github.com/skypro-008/lesson12_project_source_v3)
* `uploads` – folder for uploaded files, all files must be uploaded only in this folder
* `static` – static folder, css styles for example
* `templates` – folder for templates
* `posts.json` – file with posts data
#### Implement two blueprints:
* `main` - for show photo
* `loader` - for uploading photo
### Step 2:
* implement `main` blueprint (create, import, register it).
* Implement a form on the main page when accessing `/`
* Use the `index.html` template
* Don't forget to include the css styles from the `static` folder!
### Step 3:
* Implement search for messages in `/search/?s=<search key>` by search key
* Use the template `post_list.html`
* Reading from a file and searching for posts must be implemented in another module.
* Don't forget to rewrite css style references.
### Step 4:
* Implement `loader` blueprint (create, import, register it.).
* Implement an "add post" page when accessing `GET /post`
* Use the template `post_form.html`
* Don't forget to rewrite the style references.
### Step 5:
* Handle request when accessing `POST/post`
* Place the uploaded file in the "uploads" folder.
* Add a post to the list of posts posted in the `posts.json` file. Writing to a file must be implemented in another module.
* If the upload was successful, display the post and photo.
* Use the template `post_uploaded.html`
* If the file was not uploaded, display the message "upload failed" without a template.
* Don't forget to rewrite style references.
### Step 6:
Handle the following errors:
- File `posts.json` is missing or has a decoding error.
- The uploaded file is not an image (the extension is not jpeg or png)
- File upload error
### Step 7:
Add logging to the finished project:
`info` - when searching
`info` - if the uploaded file is not an image
`error` - if file upload error
## Hints:
When json.dump() use `ensure_ascii=False` to not decompose cyrillic characters
A `view` has already been added to the source code to upload files uploaded to `/uploads`
## How it should be implemented  
### What will be checked in the homework:
- [ ] Templates are used correctly
- [ ] Forms use the correct methods (GET or POST)
- [ ] File uploading implemented correctly
- [ ] Uploaded files are displayed correctly
- [ ] There are checks that the data has been sent
