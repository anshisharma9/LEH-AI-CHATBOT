import { useState } from "react";

import {
  FaHome,
  FaUserTie,
  FaBook,
  FaClock,
  FaBullhorn,
  FaQuestionCircle,
  FaRobot,
  FaSignOutAlt
} from "react-icons/fa";

import TeacherPage from "./TeacherPage";
import CoursePage from "./CoursePage";
import TimingPage from "./TimingPage";
import NoticePage from "./NoticePage";
import FaqPage from "./FaqPage";
import ChatPage from "./ChatPage";


function Dashboard() {

  const [activePage, setActivePage] =
    useState("dashboard");


  const logout = () => {

    localStorage.removeItem("token");
    window.location.reload();

  };


  const menuStyle = (page) => ({

    display: "flex",
    alignItems: "center",
    gap: "12px",

    padding: "14px 18px",

    borderRadius: "12px",

    marginBottom: "8px",

    cursor: "pointer",

    background:
      activePage === page
      ? "#2563eb"
      : "transparent",

    color: "white",

    fontSize: "16px",

    fontWeight: "500"

  });



  return (

    <div
      style={{

        display: "flex",

        width: "100vw",

        height: "100vh",

        background: "#f8fafc",

        overflow: "hidden"

      }}
    >


      {/* Sidebar */}

      <div
        style={{

          width: "240px",

          background: "#0f172a",

          color: "white",

          padding: "25px 15px",

          boxShadow:
            "3px 0 15px rgba(0,0,0,0.15)"

        }}
      >


        <h2
          style={{

            textAlign: "center",

            marginBottom: "25px"

          }}
        >

          LEH Admin

        </h2>


        <hr />


        <div
          style={{
            marginTop: "20px"
          }}
        >


          <div
            style={menuStyle("dashboard")}
            onClick={() =>
              setActivePage("dashboard")
            }
          >
            <FaHome />
            Dashboard
          </div>


          <div
            style={menuStyle("teachers")}
            onClick={() =>
              setActivePage("teachers")
            }
          >
            <FaUserTie />
            Teachers
          </div>


          <div
            style={menuStyle("courses")}
            onClick={() =>
              setActivePage("courses")
            }
          >
            <FaBook />
            Courses
          </div>


          <div
            style={menuStyle("timings")}
            onClick={() =>
              setActivePage("timings")
            }
          >
            <FaClock />
            Timings
          </div>


          <div
            style={menuStyle("notices")}
            onClick={() =>
              setActivePage("notices")
            }
          >
            <FaBullhorn />
            Notices
          </div>


          <div
            style={menuStyle("faq")}
            onClick={() =>
              setActivePage("faq")
            }
          >
            <FaQuestionCircle />
            FAQ
          </div>


          <div
            style={menuStyle("chat")}
            onClick={() =>
              setActivePage("chat")
            }
          >
            <FaRobot />
            AI Assistant
          </div>
                    {/* Logout Button */}

          <button
            onClick={logout}
            style={{
              marginTop: "25px",
              width: "100%",
              padding: "12px",
              background: "#dc2626",
              color: "white",
              border: "none",
              borderRadius: "10px",
              cursor: "pointer",
              fontSize: "15px",
              fontWeight: "600"
            }}
          >
            <FaSignOutAlt />
            {" "}Logout
          </button>

        </div>

      </div>


      {/* Main Content */}

      <div
        style={{
          flex: 1,
          height: "100vh",
          overflowY: "auto",
          background: "#f8fafc",
          padding:
            activePage === "chat"
              ? "0px"
              : "30px"
        }}
      >


        {/* Dashboard Home */}

        {
          activePage === "dashboard" && (

            <>
              <h1
                style={{
                  color: "#0f172a",
                  marginBottom: "25px"
                }}
              >
                Welcome to LEH Admin Panel
              </h1>


              <div
                style={{
                  display: "grid",
                  gridTemplateColumns:
                    "repeat(auto-fit, minmax(220px, 1fr))",
                  gap: "20px"
                }}
              >


                {[
                  "Teachers",
                  "Courses",
                  "Timings",
                  "FAQs"
                ].map((item) => (

                  <div
                    key={item}

                    style={{
                      background: "white",
                      padding: "25px",
                      borderRadius: "16px",
                      boxShadow:
                        "0 6px 18px rgba(0,0,0,0.08)"
                    }}
                  >

                    <h3
                      style={{
                        color: "#334155"
                      }}
                    >
                      {item}
                    </h3>


                    <h1
                      style={{
                        color: "#2563eb",
                        margin: "10px 0"
                      }}
                    >
                      0
                    </h1>


                    <p
                      style={{
                        color: "#64748b"
                      }}
                    >
                      Manage your {item.toLowerCase()} here.
                    </p>


                  </div>

                ))}


              </div>

            </>

          )
        }



        {/* Other Pages */}

        {
          activePage === "teachers" &&
          <TeacherPage />
        }


        {
          activePage === "courses" &&
          <CoursePage />
        }


        {
          activePage === "timings" &&
          <TimingPage />
        }


        {
          activePage === "notices" &&
          <NoticePage />
        }


        {
          activePage === "faq" &&
          <FaqPage />
        }


        {
          activePage === "chat" &&
          <ChatPage />
        }


      </div>


    </div>

  );

}


export default Dashboard;