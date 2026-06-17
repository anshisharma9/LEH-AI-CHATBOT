import { useState, useEffect } from "react";
import api from "../services/api";

function NoticePage() {

  const [notice, setNotice] = useState({
    title: "",
    description: ""
  });

  const [notices, setNotices] = useState([]);
  const [editId, setEditId] = useState(null);

  const handleChange = (e) => {
    setNotice({
      ...notice,
      [e.target.name]: e.target.value
    });
  };

  const fetchNotices = async () => {
    try {
      const response = await api.get("/notices");
      setNotices(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchNotices();
  }, []);

  const handleSubmit = async () => {
    try {

      if (editId) {

        await api.put(
          `/notices/${editId}`,
          notice
        );

        alert("Notice Updated");

        setEditId(null);

      } else {

        await api.post(
          "/notices",
          notice
        );

        alert("Notice Added");
      }

      setNotice({
        title: "",
        description: ""
      });

      fetchNotices();

    } catch (error) {

      console.log(error);

      alert("Error");

    }
  };

  const handleDelete = async (id) => {

    try {

      await api.delete(
        `/notices/${id}`
      );

      alert("Notice Deleted");

      fetchNotices();

    } catch (error) {

      console.log(error);

    }
  };

  const handleEdit = (notice) => {

    setNotice({
      title: notice.title,
      description: notice.description
    });

    setEditId(notice.id);
  };

  return (
    <div>

      <h2>Notice Management</h2>

      <input
        name="title"
        placeholder="Notice Title"
        value={notice.title}
        onChange={handleChange}
      />

      <br /><br />

      <textarea
        name="description"
        placeholder="Notice Description"
        value={notice.description}
        onChange={handleChange}
        rows="4"
        cols="50"
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {
          editId
            ? "Update Notice"
            : "Save Notice"
        }
      </button>

      <hr />

      <h2>Notice List</h2>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {notices.map((notice) => (
            <tr key={notice.id}>

              <td>{notice.id}</td>

              <td>{notice.title}</td>

              <td>{notice.description}</td>

              <td>

                <button
                  onClick={() =>
                    handleEdit(notice)
                  }
                >
                  Edit
                </button>

                <button
                  onClick={() =>
                    handleDelete(notice.id)
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

export default NoticePage;