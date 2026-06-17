import { useState, useEffect } from "react";
import api from "../services/api";

function TimingPage() {

  const [timing, setTiming] = useState({
    course: "",
    teacher: "",
    timing: ""
  });

  const [timings, setTimings] = useState([]);
  const [editId, setEditId] = useState(null);

  const handleChange = (e) => {
    setTiming({
      ...timing,
      [e.target.name]: e.target.value
    });
  };

  const fetchTimings = async () => {
    try {
      const response = await api.get("/timings");
      setTimings(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchTimings();
  }, []);

  const handleSubmit = async () => {

    try {

      if (editId) {

        await api.put(
          `/timings/${editId}`,
          timing
        );

        alert("Timing Updated");

        setEditId(null);

      } else {

        await api.post(
          "/timings",
          timing
        );

        alert("Timing Added");
      }

      setTiming({
        course: "",
        teacher: "",
        timing: ""
      });

      fetchTimings();

    } catch (error) {

      console.log(error);

      alert("Error");
    }
  };

  const handleDelete = async (id) => {

    try {

      await api.delete(
        `/timings/${id}`
      );

      alert("Timing Deleted");

      fetchTimings();

    } catch (error) {

      console.log(error);
    }
  };

  const handleEdit = (item) => {

    setTiming({
      course: item.course,
      teacher: item.teacher,
      timing: item.timing
    });

    setEditId(item.id);
  };

  return (
    <div>

      <h2>Timing Management</h2>

      <input
        name="course"
        placeholder="Course"
        value={timing.course}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="teacher"
        placeholder="Teacher"
        value={timing.teacher}
        onChange={handleChange}
      />

      <br /><br />

      <input
        name="timing"
        placeholder="5 PM - 6 PM"
        value={timing.timing}
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {
          editId
            ? "Update Timing"
            : "Save Timing"
        }
      </button>

      <hr />

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Course</th>
            <th>Teacher</th>
            <th>Timing</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {timings.map((item) => (
            <tr key={item.id}>

              <td>{item.id}</td>

              <td>{item.course}</td>

              <td>{item.teacher}</td>

              <td>{item.timing}</td>

              <td>

                <button
                  onClick={() =>
                    handleEdit(item)
                  }
                >
                  Edit
                </button>

                <button
                  onClick={() =>
                    handleDelete(item.id)
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

export default TimingPage;