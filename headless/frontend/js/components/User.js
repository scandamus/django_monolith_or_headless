"use strict";

import PageBase from "./PageBase.js";

export default class extends PageBase {
    constructor(params) {
        super(params);
        this.userName = "user1";
        this.setTitle(`USER: ${this.userName}`);
    }

    async getListUsers() {
        return fetch('http://localhost:8000/api/users/')
            .then(response => response.json())
            .then(data => {
                return data;
            })
            .catch(error => {
                console.error("Error fetching users:", error);
                throw error;
            });
    }

    async getHtml() {
        const listUsers = await this.getListUsers();

        if (!listUsers || listUsers.length === 0) {
            return '<div>No users found.</div>';
        }

        return `
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Last Login</th>
                    </tr>
                </thead>
                <tbody>
                    ${listUsers.map(user => `
                        <tr>
                            <td>${user.username}</td>
                            <td>${user.email}</td>
                            <td>${user.last_login}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    }
}