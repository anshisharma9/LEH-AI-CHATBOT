import { useState, useEffect } from "react";
import api from "../services/api";


function TeacherPage() {


  // ==============================
  // States
  // ==============================

  const [teachers, setTeachers] = useState([]);

  const [name, setName] = useState("");
  const [course, setCourse] = useState("");
  const [experience, setExperience] = useState("");


  // Edit Mode

  const [editingId, setEditingId] =
    useState(null);


  // ==============================
  // Load Teachers From Database
  // ==============================

  useEffect(() => {

    fetchTeachers();

  }, []);


  const fetchTeachers = async () => {

    try {

      const response =
        await api.get("/teachers/");


      setTeachers(response.data);


    } catch(error) {

      console.log(
        "Error loading teachers",
        error
      );

      alert(
        "Unable to load teachers"
      );

    }

  };


  // ==============================
  // Add New Teacher
  // ==============================

  const addTeacher = async () => {


    if (!name || !course) {

      alert(
        "Teacher name and course are required"
      );

      return;
    }


    const teacherData = {

      name: name,
      course: course,
      experience: experience || null

    };


    try {


      await api.post(
        "/teachers/",
        teacherData
      );


      alert(
        "Teacher Added Successfully"
      );


      // Reload latest data
      fetchTeachers();


      // Clear form

      setName("");
      setCourse("");
      setExperience("");


    } catch(error) {


      console.log(error);


      alert(
        "Unable to add teacher"
      );

    }

  };


  // ==============================
  // Fill Form For Editing
  // ==============================


  const editTeacher = (teacher) => {


    setEditingId(
      teacher.id
    );


    setName(
      teacher.name
    );


    setCourse(
      teacher.course
    );


    setExperience(
      teacher.experience || ""
    );


    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });


  };
    // ==============================
  // Update Teacher
  // ==============================

  const updateTeacher = async () => {

    if (!name || !course) {

      alert(
        "Teacher name and course are required"
      );

      return;
    }


    const teacherData = {

      name: name,
      course: course,
      experience: experience || null

    };


    try {

      await api.put(
        `/teachers/${editingId}`,
        teacherData
      );


      alert(
        "Teacher Updated Successfully"
      );


      setEditingId(null);

      setName("");
      setCourse("");
      setExperience("");


      fetchTeachers();


    } catch(error) {

      console.log(error);


      alert(
        "Unable to update teacher"
      );

    }

  };



  // ==============================
  // Delete Teacher
  // ==============================

  const deleteTeacher = async (id) => {


    const confirmDelete =
      window.confirm(
        "Are you sure you want to delete this teacher?"
      );


    if(!confirmDelete)
      return;


    try {


      await api.delete(
        `/teachers/${id}`
      );


      alert(
        "Teacher Deleted Successfully"
      );


      fetchTeachers();


    } catch(error) {


      console.log(error);


      alert(
        "Unable to delete teacher"
      );

    }

  };


  // ==============================
  // Cancel Edit
  // ==============================


  const cancelEdit = () => {


    setEditingId(null);

    setName("");

    setCourse("");

    setExperience("");

  };



  return (

    <div>


      <h1>
        Teacher Management
      </h1>


      {/* Form */}


      <div style={formStyle}>


        <input
          type="text"
          placeholder="Teacher Name"
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
          style={inputStyle}
        />


        <input
          type="text"
          placeholder="Course Name"
          value={course}
          onChange={(e) =>
            setCourse(e.target.value)
          }
          style={inputStyle}
        />


        <input
          type="text"
          placeholder="Experience (Optional)"
          value={experience}
          onChange={(e) =>
            setExperience(e.target.value)
          }
          style={inputStyle}
        />


        {
          editingId ? (

            <div>

              <button
                style={updateBtn}
                onClick={updateTeacher}
              >
                Update Teacher
              </button>


              <button
                style={cancelBtn}
                onClick={cancelEdit}
              >
                Cancel
              </button>

            </div>

          ) : (

            <button
              style={addBtn}
              onClick={addTeacher}
            >
              Add Teacher
            </button>

          )
        }


      </div>



      {/* Teacher Table */}


      <h2>
        Teacher List
      </h2>


      {
        teachers.length === 0 ?

        (

          <p>
            No teachers found.
          </p>

        )

        :

        (

          <table style={tableStyle}>


            <thead>


              <tr>

                <th style={thStyle}>
                  Name
                </th>

                <th style={thStyle}>
                  Course
                </th>

                <th style={thStyle}>
                  Experience
                </th>

                <th style={thStyle}>
                  Action
                </th>


              </tr>


            </thead>


            <tbody>


            {
              teachers.map((teacher) => (

              <tr key={teacher.id}>


                <td style={tdStyle}>
                  {teacher.name}
                </td>


                <td style={tdStyle}>
                  {teacher.course}
                </td>


                <td style={tdStyle}>
                  {
                    teacher.experience ||
                    "Not Mentioned"
                  }
                </td>


                <td style={tdStyle}>


                  <button
                    style={editBtn}
                    onClick={() =>
                      editTeacher(teacher)
                    }
                  >
                    Edit
                  </button>


                  <button
                    style={deleteBtn}
                    onClick={() =>
                      deleteTeacher(teacher.id)
                    }
                  >
                    Delete
                  </button>


                </td>


              </tr>

              ))
            }


            </tbody>


          </table>

        )

      }


    </div>

  );

}



// ==============================
// Styles
// ==============================


const formStyle = {

  background: "white",

  padding: "25px",

  borderRadius: "12px",

  boxShadow:
    "0 4px 12px rgba(0,0,0,0.1)",

  maxWidth: "500px"

};


const inputStyle = {

  width: "100%",

  padding: "12px",

  marginBottom: "12px",

  borderRadius: "8px",

  border: "1px solid #ccc",

  boxSizing: "border-box"

};


const addBtn = {

  background: "#2563eb",

  color: "white",

  border: "none",

  padding: "12px 18px",

  borderRadius: "8px",

  cursor: "pointer"

};


const updateBtn = {

  ...addBtn,

  marginRight: "10px"

};


const cancelBtn = {

  background: "#6b7280",

  color: "white",

  border: "none",

  padding: "12px 18px",

  borderRadius: "8px",

  cursor: "pointer"

};


const editBtn = {

  background: "#f59e0b",

  color: "white",

  border: "none",

  padding: "8px 12px",

  marginRight: "8px",

  borderRadius: "6px",

  cursor: "pointer"

};


const deleteBtn = {

  background: "#dc2626",

  color: "white",

  border: "none",

  padding: "8px 12px",

  borderRadius: "6px",

  cursor: "pointer"

};


const tableStyle = {

  width: "100%",

  marginTop: "20px",

  borderCollapse: "collapse",

  background: "white",

  boxShadow:
    "0 4px 12px rgba(0,0,0,0.1)"

};


const thStyle = {

  background: "#0f172a",

  color: "white",

  padding: "14px"

};


const tdStyle = {

  textAlign: "center",

  padding: "14px",

  borderBottom: "1px solid #ddd"

};


export default TeacherPage;