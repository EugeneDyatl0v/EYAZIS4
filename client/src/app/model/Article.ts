export interface Article {
  id?: string,
  title: string,
  text: string,
  source_language: string,
  is_original: boolean,
  original_article_id?: string
}
