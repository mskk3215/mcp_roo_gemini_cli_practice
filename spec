# User Authentication TODO App Implementation Plan

This document outlines the plan to implement a TODO application with user authentication.

## 1. Core Features

*   **User Authentication:**
    *   User registration (signup)
    *   User login
    *   User logout
    *   Protected routes to ensure only authenticated users can access the TODO list.
*   **TODO Management:**
    *   Create new TODO items.
    *   View the list of TODO items.
    *   Mark TODO items as complete.
    *   Delete TODO items.

## 2. Technology Stack

*   **Framework:** Next.js (using App Router)
*   **Language:** TypeScript
*   **Styling:** Tailwind CSS
*   **Authentication:** `next-auth` library
*   **Database:** For this prototype, we will use a simple file-based approach (JSON files) to store users and their TODOs. This can be easily swapped out for a more robust database like PostgreSQL or MongoDB in the future.

## 3. Implementation Steps

### Step 1: Project Setup & Dependency Installation

1.  **Install `next-auth`:** Add the `next-auth` library to the project.
    ```bash
    npm install next-auth
    ```
2.  **Install `bcrypt` for password hashing:**
    ```bash
    npm install bcrypt
    npm install --save-dev @types/bcrypt
    ```

### Step 2: Authentication Backend

1.  **Configure `next-auth`:**
    *   Create the dynamic API route `src/app/api/auth/[...nextauth]/route.ts`.
    *   Configure the `CredentialsProvider` for email and password authentication.
    *   Implement the `authorize` function to validate user credentials against the stored user data.
    *   Set up session management using JWT.
2.  **Password Hashing:**
    *   Use `bcrypt` to hash user passwords upon registration and compare them during login.
3.  **User Data Storage:**
    *   Create a simple data access layer to manage users in a `users.json` file. This will include functions for finding a user by email and creating a new user.

### Step 3: Authentication Frontend

1.  **Create Login Page (`src/app/login/page.tsx`):**
    *   Build a form with email and password fields.
    *   Use the `signIn` function from `next-auth/react` to handle form submission.
    *   Provide feedback for successful or failed login attempts.
2.  **Create Signup Page (`src/app/signup/page.tsx`):**
    *   Build a form for user registration.
    *   Create a new API endpoint (e.g., `/api/register`) to handle the creation of a new user.
    *   The signup page will POST to this endpoint.
3.  **Session Provider:**
    *   Wrap the root layout (`src/app/layout.tsx`) with a `SessionProvider` component to make session data available throughout the app.
4.  **Protected Routes:**
    *   Create a `middleware.ts` file at the root of the project to protect the TODO list page, redirecting unauthenticated users to the login page.

### Step 4: TODO API Backend

1.  **Create TODO API Routes:**
    *   `POST /api/todos`: Create a new TODO item for the authenticated user.
    *   `GET /api/todos`: Get all TODO items for the authenticated user.
    *   `PUT /api/todos/[id]`: Update a TODO item (e.g., mark as complete).
    *   `DELETE /api/todos/[id]`: Delete a TODO item.
2.  **TODO Data Storage:**
    *   Create a `todos.json` file to store TODO items. Each TODO will be associated with a `userId`.
    *   The API routes will read from and write to this file, ensuring users can only access their own TODOs.

### Step 5: TODO Frontend

1.  **Create TODO Page (`src/app/todos/page.tsx`):**
    *   This will be the main page for managing TODOs.
    *   Fetch the user's TODOs from the `/api/todos` endpoint.
    *   Display the list of TODOs.
2.  **Create Components:**
    *   `TodoItem.tsx`: A component to display a single TODO item with buttons for marking as complete and deleting.
    *   `AddTodoForm.tsx`: A form component to add a new TODO item.
    *   `LogoutButton.tsx`: A client component that uses the `signOut` function from `next-auth/react`.
3.  **State Management:**
    *   Use React's `useState` and `useEffect` hooks to manage the state of the TODO list (fetching, adding, deleting items).

## 4. File Structure Overview

```
/
├── middleware.ts
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/
│   │   │   │   └── [...nextauth]/
│   │   │   │       └── route.ts
│   │   │   ├── register/
│   │   │   │   └── route.ts
│   │   │   └── todos/
│   │   │       ├── route.ts
│   │   │       └── [id]/
│   │   │           └── route.ts
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── signup/
│   │   │   └── page.tsx
│   │   ├── todos/
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   ├── AddTodoForm.tsx
│   │   ├── TodoItem.tsx
│   │   └── LogoutButton.tsx
│   └── lib/
│       ├── data.ts       // Functions for accessing users.json and todos.json
│       └── auth.ts       // next-auth configuration options
├── data/                 // Directory for JSON data files
│   ├── users.json
│   └── todos.json
...
```
