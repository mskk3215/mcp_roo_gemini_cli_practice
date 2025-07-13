"use client";

export default function LogoutButton() {
  const handleLogout = () => {
    // In a real app, this would call next-auth's signOut()
    alert("Logged out!");
  };

  return (
    <button
      onClick={handleLogout}
      className="px-4 py-2 font-semibold text-white bg-gray-600 rounded-lg hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
    >
      Logout
    </button>
  );
}
