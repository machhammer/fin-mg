import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { User } from '../models/user';

import { environment } from '../../environments/environment';


@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient) { }

    getAll() {
        return this.http.get<User[]>(environment.serverUrl + '/users');
    }


    user(email: String) {
        return this.http.post(environment.serverUrl + '/user', email);
    }

    user_update(email: String) {
        return this.http.post(environment.serverUrl + '/user_update', email);
    }


    register(email: String, password: String, firstName: String, lastName: String) {
        return this.http.post(environment.serverUrl + `/register`, {email, password, firstName, lastName});
    }

    update(user: User) {
        return this.http.put(environment.serverUrl +'/users/${user.id}', user);
    }

    delete(id: number) {
        return this.http.delete(environment.serverUrl + 'users/${id}');
    }
}