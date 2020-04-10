import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Index } from '../models/index';

import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { map, tap } from 'rxjs/operators';



@Injectable({ providedIn: 'root' })
export class ReferenceService {
    constructor(private http: HttpClient) { }

    getIndices() {
        return this.http
            .get(environment.serverUrl + `/indices`)
            
    }

    getEquities() {
        return this.http
            .get(environment.serverUrl + `/equities`)
            
    }

    getLooser() {
        return this.http
            .get(environment.serverUrl + `/looser`)
            
    }

    getWinner() {
        return this.http
            .get(environment.serverUrl + `/winner`)
            
    }

}