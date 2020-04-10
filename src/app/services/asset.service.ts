import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';


@Injectable({ providedIn: 'root' })
export class AssetService {
    constructor(private http: HttpClient) { }

    search(searchValue) {
        console.log("**********************: " + searchValue)
        return this.http.get(environment.serverUrl + '/asset/' + searchValue);
    }

}