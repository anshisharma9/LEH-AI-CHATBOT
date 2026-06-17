import { useState, useEffect } from "react";
import api from "../services/api";

function FaqPage() {

  const [faq, setFaq] = useState({
    question: "",
    answer: ""
  });

  const [faqs, setFaqs] = useState([]);
  const [editId, setEditId] = useState(null);

  const handleChange = (e) => {
    setFaq({
      ...faq,
      [e.target.name]: e.target.value
    });
  };

  const fetchFaqs = async () => {
    try {
      const response = await api.get("/faq");
      setFaqs(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchFaqs();
  }, []);

  const handleSubmit = async () => {

    try {

      if (editId) {

        await api.put(
          `/faq/${editId}`,
          faq
        );

        alert("FAQ Updated");

        setEditId(null);

      } else {

        await api.post(
          "/faq",
          faq
        );

        alert("FAQ Added");
      }

      setFaq({
        question: "",
        answer: ""
      });

      fetchFaqs();

    } catch (error) {

      console.log(error);

      alert("Error");
    }
  };

  const handleDelete = async (id) => {

    try {

      await api.delete(`/faq/${id}`);

      alert("FAQ Deleted");

      fetchFaqs();

    } catch (error) {

      console.log(error);
    }
  };

  const handleEdit = (faq) => {

    setFaq({
      question: faq.question,
      answer: faq.answer
    });

    setEditId(faq.id);
  };

  return (
    <div>

      <h2>FAQ Management</h2>

      <input
        name="question"
        placeholder="Question"
        value={faq.question}
        onChange={handleChange}
      />

      <br /><br />

      <textarea
        name="answer"
        placeholder="Answer"
        value={faq.answer}
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {
          editId
            ? "Update FAQ"
            : "Save FAQ"
        }
      </button>

      <hr />

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Question</th>
            <th>Answer</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {faqs.map((faq) => (
            <tr key={faq.id}>

              <td>{faq.id}</td>

              <td>{faq.question}</td>

              <td>{faq.answer}</td>

              <td>

                <button
                  onClick={() =>
                    handleEdit(faq)
                  }
                >
                  Edit
                </button>

                <button
                  onClick={() =>
                    handleDelete(faq.id)
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

export default FaqPage;