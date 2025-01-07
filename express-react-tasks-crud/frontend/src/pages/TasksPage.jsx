import { useTask } from "@/context/TasksContext";
import React, { useEffect } from "react";
import { ImFileEmpty } from "react-icons/im";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "../components/ui/card";
import { Label } from "../components/ui/label";
import { Button } from "@/components/ui/button";
import { ButtonLink } from "@/components/ui/ButtonLink";
function TasksPage() {
  const { getTasks, tasks ,deleteTask} = useTask();

  useEffect(() => {
    getTasks();
  }, []);
  
  return (
    
        <>
    {tasks.length === 0 && (
      <div className="flex justify-center items-center p-10">
        <div>
        <ImFileEmpty className="text-6xl text-gray-400 m-auto my-2" />
          <h1 className="font-bold text-xl">
            No tasks yet, please add a new task
          </h1>
        </div>
      </div>
    )}
    

      <div className="grid sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3">
        {tasks.map((task) => (
          <Card className="bg-zinc-800 text-white " key={task._id}>
            <header className="flex justify-between">
              <h1 className="text-2xl font-bold ml-2">{task.title}</h1>
              <div className="flex gap-x-2 items-center mt-2 mx-2">
               
                <ButtonLink to={`/tasks/${task._id}`} >Edit</ButtonLink>
                <Button className=" bg-red-700 text-xs size-min "
                onClick={()=>{
                    deleteTask(task._id)
                }}
                >Delete</Button>
              </div>
            </header>

            <CardContent>
              <p className="">{task.description}</p>
            </CardContent>
            <div></div>
            <p className="flex justify-center">
              {task.date &&
                new Date(task.date).toLocaleDateString("en-US", {
                  weekday: "long",
                  year: "numeric",
                  month: "long",
                  day: "numeric",
                })}
            </p>
            
          </Card>
        ))}
      </div>
   </>


    
  );
}

export default TasksPage;
