import React, { useState } from "react";
import Create from "./create";

const Home = () => {
  const [Todos, setTodos] = useState([]);
  return (
<div className="w-full bg-slate-900 min-h-screen ">
    <div className="bg-slate-200 w-[500px] h-[400px] translate-x-32 px-6">
    <>
      <div className="w-full flex justify-center">
        <h2 className="text-4xl font-bold text-green-500">Todo list</h2>
      </div>
      <div className="text-black flex space-x-3">
       <h1 className="text-3xl">Hello</h1>
       <h2 className="text-3xl text-green-600">Jireh</h2>
       </div>
       <div className="text-black">
        <p>You have the following tasks</p></div>
       
      
      <div className="p-6 space-y-5 text-center">
      <h2 className="text-2xl w-[300px] h-[70px] bg-slate-100 rounded-md ">Singing</h2>
      <h2 className="text-2xl w-[300px] h-[70px] bg-slate-100 rounded-md">Writing stories</h2>
      </div>
      <Create />
      {Todos.length === 0 ? (
        <div>
          <h1>No record</h1>
        </div>
      ) : (
        Todos.map((todo) => {
          <div>{todo}</div>;
        })
      )}
    </>
    </div>
</div>
  );
};
export default Home;
