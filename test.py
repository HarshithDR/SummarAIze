import json
# result_from_brx = asyncio.run(brx_fetch(promt))
# result_from_brx = data
# url_from_fal = fal_api_fun(extract_url(result_from_brx))
# print(url_from_fal)
url_from_fal = {'video': {'url': 'https://storage.googleapis.com/isolate-dev-hot-rooster_toolkit_bucket/github_110602490/a513a24218624a3d9baa385f3b81d5ec_reenc-tmpcpxws4_t.mp4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gke-service-account%40isolate-dev-hot-rooster.iam.gserviceaccount.com%2F20240407%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240407T074516Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=06fa8fb91c07f6f98cf71a4454472dad82e17d6634d072a0979da83aede84356a75decc35685f3c1276070e0f3700b0c66a4c6bb81ec1e3eb64b4621e0dfedbbefb62aa85401f403fd046d8ab397c7a956d7aed6ff623ca4292b695f4f5ddd7e76f58e4f406ee09cc0b5863b5aa735b6b38c403506a430e30da5a735d49ed6c2c780cc7dd892b3db7c5b4530970153fc2c98ee5d3d56655e3431fe4cddf5b555f34d9e9b2806fe924f1701c63b3f6bbdc7ac3c5554e0e995f86e599562f82aff32cf4fbd583aeb9797238345760c7732af0f2825fd90736bc653cb3a59ccdc8a76a30b494d7705b05a2557a28f4b2641e383f650676dbafa0975530efa230c81', 'content_type': 'video/mp4', 'file_name': 'reenc-tmpcpxws4_t.mp4', 'file_size': 1067637}, 'seed': 9413975911279377712}
parsed_data = url_from_fal
video_url = parsed_data['video']['url']
# save_path = "Backend\\summaraize_app\\video_generation"
# download_video(video_url,save_path)

print(type(video_url))