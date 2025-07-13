"use client";

import { useState } from "react";
import AddTodoForm from "@/components/AddTodoForm";
import TodoItem, { type Todo } from "@/components/TodoItem";
import LogoutButton from "@/components/LogoutButton";

// Mock data for initial UI development
const initialTodos: Todo[] = [
  { id: 1, title: "Learn Next.js", completed: true },
  { id: 2, title: "Build a TODO App", completed: false },
  { id: 3, title: "Deploy to Vercel", completed: false },
];

export default function TodoPage() {
  const [todos, setTodos] = useState<Todo[]>(initialTodos);

  const handleAddTodo = (title: string) => {
    const newTodo: Todo = {
      id: Date.now(),
      title,
      completed: false,
    };
    setTodos([...todos, newTodo]);
  };

  const handleToggleComplete = (id: number, completed: boolean) => {
    setTodos(
      todos.map((todo) => (todo.id === id ? { ...todo, completed } : todo))
    );
  };

  const handleDelete = (id: number) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
        <header className="flex items-center justify-between">
          <h1 className="text-3xl font-bold text-gray-900">TODO App</h1>
          <LogoutButton />
        </header>
        
        <AddTodoForm onAddTodo={handleAddTodo} />

        <ul className="space-y-4">
          {todos.map((todo) => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggleComplete={handleToggleComplete}
              onDelete={handleDelete}
            />
          ))}
        </ul>
      </div>
    </div>
  );
}
