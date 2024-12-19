import {Injectable} from '@angular/core';
import {Constants} from '../Constants';
import {HttpClient} from '@angular/common/http';
import {ResponseData} from '../model/ResponseData';
import {Article} from '../model/Article';
import {NormalForm} from '../model/NormalForm';
import {Word} from '../model/Word';
import {Sentence} from '../model/Sentence';

@Injectable({
  providedIn: 'root'
})
export class ArticleServiceService {
  url = Constants.BACKEND_URL + "/articles/";

  constructor(private http: HttpClient) {  }

  getAllArticles() {
    return this.http.get<ResponseData<Array<Article>>>(this.url)
  }

  createArticle(article: Article) {
    return this.http.post<ResponseData<Article>>(this.url, article)
  }

  deleteArticle(id: string) {
    return this.http.delete(this.url, { params:{article_id: id} })
  }

  getArticle(id: string) {
    return this.http.get<ResponseData<Article>>(this.url+`${id}/`)
  }

  translateArticle(id: string, param: string) {
        return this.http.get<ResponseData<Article>>(this.url+`translate/${id}/`, { params: {target_language:param} })
  }

  getWords(id: string) {
        return this.http.get<ResponseData<Array<NormalForm>>>(this.url+`${id}/words/`)
  }

  getSpeechParts(id: string) {
      return this.http.get<ResponseData<Array<Word>>>(this.url+`${id}/words/speech-parts/`)
  }

  getSyntax(id: string) {
      return this.http.get<ResponseData<Array<Sentence>>>(this.url+`${id}/syntax/`)
  }

}
