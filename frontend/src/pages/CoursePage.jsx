import { useState, useEffect } from "react";
import api from "../services/api";

function CoursePage() {

  const [course, setCourse] = useState({
    course_name: "",
    fees: "",
    duration: "",
    description: ""
  });

  const [courses, setCourses] = useState([]);
  const [editId, setEditId] = useState(null);

  const handleChange = (e) => {
    setCourse({
      ...course,
      [e.target.name]: e.target.value
    });
  };

  const fetchCourses = async () => {
    try {
      const response = await api.get("/courses");
      setCourses(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const handleSubmit = async () => {
    try {

      if (editId) {

        await api.put(
          `/courses/${editId}`,
          course
        );

        alert("Course Updated");

        setEditId(null);

      } else {

        await api.post(
          "/courses",
          course
        );

        alert("Course Added");
      }

      setCourse({
        course_name: "",
        fees: "",
        duration: "",
        description: ""
      });

      fetchCourses();

    } catch (error) {

      console.log(error);

      alert("Error");
    }
  };

  const handleDelete = async (id) => {

    try {

      await api.delete(`/courses/${id}`);

      alert("Course Deleted");

      fetchCourses();

    } catch (error) {

      console.log(error);

    }
  };

  const handleEdit = (course) => {

    setCourse({
      course_name: course.course_name,
      fees: course.fees,
      duration: course.duration,
      description: course.description
    });

    setEditId(course.id);
  };

  return (
    <div>

      <h2>Course Management</h2>

      <input
        name="course_name"
        placeholder="Course Name"
        value={course.course_name}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="fees"
        placeholder="Fees"
        value={course.fees}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="duration"
        placeholder="Duration"
        value={course.duration}
        onChange={handleChange}
      />

      <br /><br />

      <textarea
        name="description"
        placeholder="Description"
        value={course.description}
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {editId ? "Update Course" : "Save Course"}
      </button>

      <hr />

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Course</th>
            <th>Fees</th>
            <th>Duration</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {courses.map((course) => (
            <tr key={course.id}>

              <td>{course.id}</td>

              <td>{course.course_name}</td>

              <td>{course.fees}</td>

              <td>{course.duration}</td>

              <td>

                <button
                  onClick={() =>
                    handleEdit(course)
                  }
                >
                  Edit
                </button>

                <button
                  onClick={() =>
                    handleDelete(course.id)
                  }
                >
                  Delete
                </button>

              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default CoursePage;