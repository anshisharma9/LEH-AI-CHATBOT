import { useState, useEffect, useRef } from "react";
import api from "../services/api";


function ChatPage() {


  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);


  const chatEndRef = useRef(null);



  // Initial Welcome Message

  useEffect(() => {

    setMessages([
      {
        sender: "bot",

        text: `Welcome to Learning Education Hub.

I am your LEH AI Assistant.

I can guide you with courses, trainers, admissions, batch timings, placements and career decisions.

How can I help you today?`,


        options: [

          "Explore Courses",

          "Meet Trainers",

          "Batch Timings",

          "Admission Process",

          "Placement Support",

          "Career Guidance",

          "About LEH"

        ]

      }

    ]);

  }, []);



  // Auto Scroll

  useEffect(() => {


    chatEndRef.current?.scrollIntoView({

      behavior: "smooth"

    });


  }, [messages, loading]);




  // Send Message


  const sendMessage = async (customText = null) => {


    const text = customText || message;


    if (!text.trim()) return;



    const userMessage = {

      sender: "user",

      text

    };



    setMessages(prev => [

      ...prev,

      userMessage

    ]);


    setMessage("");

    setLoading(true);



    try {


      const response = await api.post(

        "/chat/",

        {

          message: text

        }

      );



      const botMessage = {


        sender: "bot",


        text: response.data.answer,


        options:

          response.data.options || []

      };



      setMessages(prev => [

        ...prev,

        botMessage

      ]);



    } catch (error) {


      console.log(error);



      setMessages(prev => [

        ...prev,

        {

          sender: "bot",

          text: `Sorry, I am unable to respond right now.

Please try again after some time.`

        }

      ]);



    } finally {


      setLoading(false);

    }


  };
    return (

    <div
      style={{
        height: "100%",
        background: "#f5f7fb",
        display: "flex",
        flexDirection: "column"
      }}
    >


      {/* Header */}

      <div
        style={{
          background: "#0f172a",
          color: "white",
          padding: "18px 25px",
          borderBottom: "1px solid #1e293b"
        }}
      >

        <h2
          style={{
            margin: 0,
            fontSize: "22px",
            fontWeight: "600"
          }}
        >
          LEH AI Assistant
        </h2>


        <p
          style={{
            margin: "5px 0 0 0",
            color: "#cbd5e1",
            fontSize: "14px"
          }}
        >
          Your Career and Admission Counselor
        </p>


      </div>



      {/* Chat Area */}


      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "25px"
        }}
      >


        {

          messages.map((msg, index) => (

            <div
              key={index}
              style={{
                marginBottom: "22px",
                display: "flex",
                justifyContent:
                  msg.sender === "user"
                    ? "flex-end"
                    : "flex-start"
              }}
            >


              <div
                style={{
                  maxWidth: "70%",
                  background:
                    msg.sender === "user"
                      ? "#2563eb"
                      : "#ffffff",

                  color:
                    msg.sender === "user"
                      ? "white"
                      : "#111827",

                  padding: "16px 18px",

                  borderRadius:
                    msg.sender === "user"
                      ? "18px 18px 4px 18px"
                      : "18px 18px 18px 4px",

                  boxShadow:
                    "0 3px 12px rgba(0,0,0,0.08)",

                  lineHeight: "1.6"
                }}
              >


                {/* Message Name */}

                <div
                  style={{
                    fontWeight: "600",
                    marginBottom: "8px",
                    fontSize: "14px"
                  }}
                >

                  {
                    msg.sender === "user"
                      ? "You"
                      : "LEH AI Assistant"
                  }

                </div>



                {/* Message Text */}


                <div
                  style={{
                    whiteSpace: "pre-line",
                    fontSize: "15px"
                  }}
                >
                  {msg.text}
                </div>



                {/* Option Buttons */}


                {
                  msg.options &&
                  msg.options.length > 0 &&

                  <div
                    style={{
                      marginTop: "15px",
                      display: "flex",
                      flexWrap: "wrap",
                      gap: "8px"
                    }}
                  >

                    {
                      msg.options.map((option, i) => (

                        <button
                          key={i}

                          onClick={() =>
                            sendMessage(option)
                          }

                          style={{

                            background: "#e2e8f0",

                            color: "#1e293b",

                            border: "none",

                            padding: "8px 14px",

                            borderRadius: "18px",

                            cursor: "pointer",

                            fontSize: "13px",

                            fontWeight: "500"

                          }}

                        >

                          {option}

                        </button>

                      ))
                    }


                  </div>

                }


              </div>


            </div>

          ))

        }



        {/* Typing Indicator */}


        {
          loading && (

            <div
              style={{

                background: "white",

                width: "180px",

                padding: "15px",

                borderRadius: "16px",

                boxShadow:
                  "0 3px 10px rgba(0,0,0,0.08)"

              }}
            >

              <strong>
                LEH AI Assistant
              </strong>

              <br />

              Thinking...

            </div>

          )

        }


        <div ref={chatEndRef}></div>


      </div>
            {/* Input Area */}

      <div
        style={{
          background: "#ffffff",
          padding: "18px 25px",
          borderTop: "1px solid #e2e8f0",
          display: "flex",
          alignItems: "center",
          gap: "12px"
        }}
      >


        {/* Text Input */}

        <input

          type="text"

          value={message}

          placeholder="Ask about courses, admission, trainers or your career path..."

          onChange={(e) =>
            setMessage(e.target.value)
          }


          onKeyDown={(e) => {

            if (e.key === "Enter") {

              sendMessage();

            }

          }}


          style={{

            flex: 1,

            height: "50px",

            padding: "0 18px",

            border: "1px solid #cbd5e1",

            borderRadius: "30px",

            outline: "none",

            fontSize: "15px",

            background: "#f8fafc"

          }}

        />


        {/* Send Button */}

        <button

          onClick={() =>
            sendMessage()
          }


          style={{

            background: "#2563eb",

            color: "#ffffff",

            border: "none",

            padding: "0 24px",

            height: "50px",

            borderRadius: "30px",

            cursor: "pointer",

            fontSize: "15px",

            fontWeight: "600",

            transition: "0.3s"

          }}

        >

          Send

        </button>


      </div>


    </div>

  );

}


export default ChatPage;