import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Injectable({ providedIn: 'root' })
export class AssetService {
    constructor(private http: HttpClient) { }

    search(searchValue) {
        console.log("**********************: " + searchValue)
        return this.http.get('http://localhost:8000/asset/' + searchValue);
    }

}