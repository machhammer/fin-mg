import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Index } from '../models/index';

import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';


@Injectable({ providedIn: 'root' })
export class ReferenceService {
    constructor(private http: HttpClient) { }

    getIndices() {
        return this.http
            .get(`http://localhost:8000/indices`)
            
    }

    getEquities() {
        return this.http
            .get(`http://localhost:8000/equities`)
            
    }
}