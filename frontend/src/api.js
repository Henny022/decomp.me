const { API_BASE } = import.meta.env

const commonOpts = {
    credentials: "include",
    cache: "reload",
}

export async function get(url, cache = false) {
    const response = await fetch(API_BASE + url, {
        ...commonOpts,
        cache: cache ? "default" : "reload",
    })

    if (!response.ok) {
        throw new Error(response.status)
    }

    return await response.json()
}

export async function post(url, body) {
    if (typeof body != "string") {
        body = JSON.stringify(body)
    }

    const response = await fetch(API_BASE + url, {
        ...commonOpts,
        method: "POST",
        body,
        headers: {
            'Content-Type': 'application/json',
        },
    })

    if (!response.ok) {
        throw new Error(response.status)
    }

    return await response.json()
}
