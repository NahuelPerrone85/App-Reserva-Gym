import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { Link } from "react-router-dom";

export const CreateAdmin = () => {

    const { store, dispatch } = useGlobalReducer()

    useEffect(() => {
    
    }, [])

    return (
        <div className="d-flex justify-content-center mt-5">
            <form>
                <div className="mb-3">
                    <label for="exampleInputName1" className="form-label">Name</label>
                    <input type="name" className="form-control" id="exampleInputName1" aria-describedby="nameHelp" />
                </div>
                <div className="mb-3">
                    <label for="exampleInputLastName1" className="form-label">Last Name</label>
                    <input type="lastName" className="form-control" id="exampleInputLastName1" aria-describedby="lastNameHelp" />
                </div>

                <div className="mb-3">
                    <label for="exampleInputEmail1" className="form-label">Email address</label>
                    <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                </div>
                <div className="mb-3">
                    <label for="exampleInputPassword1" className="form-label">Password</label>
                    <input type="password" className="form-control" id="exampleInputPassword1" />
                </div>
                <button type="singUp" className="btn btn-primary">Create</button>
                <Link to="/">
                <button type="back" className="btn btn-primary ms-5">Back</button>
                </Link>
            </form>
        </div>
    );
}; 