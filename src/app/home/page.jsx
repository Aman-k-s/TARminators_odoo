"use client";
import React, { useState } from "react";
import Layout from "../component/layout";
import SwapModal from "../component/swapmodel";
import Pagination from "../component/pagination"; // adjust path if needed

const mockUsers = [
  {
    id: 1,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 2,
    name: "Tuhin",
    location: "Chandigarh",
    skills: ["Python", "Machine Learning"],
  },
  {
    id: 3,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 4,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 5,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 5,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 6,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 7,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
  {
    id: 8,
    name: "Aman",
    location: "Delhi",
    skills: ["Photoshop", "Excel"],
  },
];

export default function Home() {
  const [modalOpen, setModalOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 3; // You can change this as needed

  return (
    <Layout>
      <SwapModal isOpen={modalOpen} onClose={() => setModalOpen(false)} />
      <h2 className="text-xl font-bold mb-4">Browse Users</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {mockUsers
          .slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage)
          .map((user) => (
            <div key={user.id} className="bg-gray-800 p-4 rounded-xl shadow">
              <h3 className="text-lg font-medium">{user.name}</h3>
              <p className="text-sm text-gray-400">{user.location}</p>
              <div className="mt-2 flex flex-wrap gap-2">
                {user.skills.map((skill) => (
                  <span
                    key={skill}
                    className="text-sm bg-teal-600 text-white px-2 py-1 rounded"
                  >
                    {skill}
                  </span>
                ))}
              </div>
              <button
                className="mt-4 bg-teal-500 hover:bg-teal-600 px-4 py-2 rounded"
                onClick={() => setModalOpen(true)}
              >
                Request Swap
              </button>
            </div>
          ))}
      </div>
      <Pagination
        currentPage={currentPage}
        totalPages={Math.ceil(mockUsers.length / itemsPerPage)}
        onPageChange={(page) => setCurrentPage(page)}
      />
    </Layout>
  );
}
// Then use <SwapModal isOpen={modalOpen} onClose={() => setModalOpen(false)} />
